CREATE TABLE Supply (
	ItemId int PRIMARY KEY,
	ItemPrice numeric(2) NOT NULL CHECK(ItemPrice > 0),
	ItemName varchar(30) NOT NULL
);


CREATE TABLE Flower (
	ItemId int NOT NULL
	    REFERENCES Supply (ItemID)
        ON DELETE CASCADE,
	FlowerColor varchar(15) NOT NULL,
	PRIMARY KEY (ItemId)
);


CREATE TABLE Music (
	ItemId int NOT NULL
	    REFERENCES Supply (ItemID)
        ON DELETE CASCADE,
	Genre varchar(15) NOT NULL,
	Artist varchar(35) NOT NULL,
	PRIMARY KEY (ItemId)
);


CREATE TABLE Food (
    ItemId int NOT NULL
        REFERENCES Supply (ItemID)
        ON DELETE CASCADE,
	FoodType varchar(15) NOT NULL,
	FoodIngredients varchar(255) NOT NULL,
	PRIMARY KEY (ItemId)
);

CREATE TABLE "user" (
	UserID SERIAL PRIMARY KEY,
	FirstName varchar(255) NOT NULL,
	LastName varchar(255) NOT NULL,
	Email varchar(255) NOT NULL UNIQUE,
	Password varchar(255) NOT NULL
);


CREATE TABLE Supplier (
	SupplierUserID int NOT NULL
        REFERENCES "user" (UserID)
        ON DELETE CASCADE,
	BankingAccount varchar(255) NOT NULL,
	WebsiteLink varchar(255),
	ContactEmail varchar(255) NOT NULL,
	PRIMARY KEY (SupplierUserID)
);


CREATE TABLE Client (
	ClientUserID int NOT NULL
	    REFERENCES "user" (UserID)
        ON DELETE CASCADE,
	AccountBalance decimal(9, 2) DEFAULT 0
        CHECK(AccountBalance >= 000000000.00),
    PRIMARY KEY (ClientUserID)
);


CREATE TABLE Planner (
	PlannerUserID int NOT NULL
        REFERENCES "user" (UserID)
        ON DELETE CASCADE,
	Position varchar(255),
	Rate int CHECK (Rate > 0),
	BankingAccount varchar(255),
	PRIMARY KEY (PlannerUserID)
);


CREATE TABLE PhoneNumber (
	UserID int NOT NULL
        REFERENCES "user" (UserId)
        ON DELETE CASCADE,
	PhoneNumber int NOT NULL,
	TypeOfPhone varchar(30),
	PRIMARY KEY (UserID, PhoneNumber)
);


CREATE TABLE ProvidedBy (
	ItemId int NOT NULL
        REFERENCES SUPPlY (ItemId)
        ON DELETE CASCADE,
	SupplierUserID int NOT NULL
        REFERENCES Supplier (SupplierUserID)
        ON DELETE CASCADE,
	Quantity int CHECK(Quantity > 0),
	PRIMARY KEY (ItemID)
);


CREATE TABLE Location (
	LocationID SERIAL PRIMARY KEY,
	LocationCapacity int NOT NULL CHECK(LocationCapacity > 0),
	LocationOpenHour int NOT NULL,
	LocationCloseHour int NOT NULL,
	LocationName varchar(255) NOT NULL,
	LocationAddress varchar(255) NOT NULL,
    LocationPrice int NOT NULL CHECK(LocationPrice > 0)
);


CREATE TABLE Loan_Provider (
	InstitutionID int NOT NULL PRIMARY KEY,
	PhoneNumber int NOT NULL,
	EmbeddedURL varchar(255) NOT NULL
);


CREATE TABLE Event (
	EventID SERIAL PRIMARY KEY,
	ClientUserID int NOT NULL
	    REFERENCES Client (ClientUserID)
	    ON DELETE CASCADE,
    PlannerUserID int
        REFERENCES Planner (PlannerUserID)
        ON DELETE SET NULL,
	LocationID int
	    REFERENCES Location (LocationID)
        ON DELETE SET NULL,
	InstitutionID int
	    REFERENCES Loan_Provider (InstitutionID)
        ON DELETE SET NULL,
    EventName varchar(255) NOT NULL,
    EventBudget int CHECK(EventBudget >= 0),
    PlanningFee int CHECK(PlanningFee >= 0),
    StartTimestamp timestamp,
    EndTimestamp timestamp CHECK(EndTimestamp > StartTimestamp)
);


CREATE TABLE "order" (
	ItemID int NOT NULL
	    REFERENCES SUPPLY (ItemId)
        ON DELETE CASCADE,
	SupplierUserID int NOT NULL
        REFERENCES Supplier (SupplierUserID)
        ON DELETE CASCADE,
	ClientUserID int NOT NULL
        REFERENCES Client (ClientUserID)
        ON DELETE CASCADE,
	EventID int NOT NULL REFERENCES Event (EventID),
	Quantity int Check(Quantity > 0),
	PRIMARY KEY (ItemID, SupplierUserID, ClientUserID, EventID)
);
