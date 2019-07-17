#!/usr/bin/python

import sys

import psycopg2
import os
import getopt
import ast




conn_string = "host="+ "db-image" +" port="+ "5432" +" dbname=postgres"+ " user=postgres" \
+" password=";





#python3.7 main_backend.py -c insert -t user "2,andr,tam,123,qqq@uwaterloo.ca"
def insert_data(vendor_name, value):
    """ insert a new vendor into the vendors table """
    conn=psycopg2.connect(user = "postgres", password = "", host = "localhost",port = "5432", database = "postgres");
    cursor = conn.cursor()

    sql_client = """INSERT into Client values (%s, %s);"""
    sql_flower = """INSERT into Flower values (%s, '%s');""" #(id, flower_color)
    sql_music = """INSERT into Music values (%s, '%s', '%s');"""#(id, genre, artist)
    sql_food = """INSERT into Food values (%s, '%s', '%s');"""#(id, foodtype, FoodIngredients )
    sql_user ="""INSERT into "user" values (%s, '%s', '%s', '%s', '%s');"""#(id, fname,lname,pass,email)
    sql_supplier ="""INSERT into user Supplier values (%s, '%s', '%s', '%s');"""#(id, bank,web, email)
    sql_planner = """INSERT into user Planner values (%s, '%s', '%s', '%s', '%s');"""#(id, position,rate, bankacc)

    options = {"client" : sql_client,
           "flower" : sql_flower,
           "music" : sql_music,
           "food" : sql_food,
           "\"user\"" : sql_user,
           "supplier" : sql_supplier,
           "planner" : sql_planner,
    }

    sql_ins = options[vendor_name];
    delim_val = tuple(value.split(","));
    sql_ins = sql_ins % delim_val;

    #conn = None
    vendor_id = None
    try:
        # connect to the PostgreSQL database
        #conn = psycopg2.connect(conn_string)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql_ins)
        # get the generated id back
        #vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        print("Insert to %s succeed" % vendor_name);
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return vendor_id

test_dic = {"id" : "2",
            "flower_color": "red"}

#main_backend.py -c select -t user -s FirstName,LastName -w "{\"userid\" : 3}"
def select_all_where(table, selected_item,where, order_by):
    """ query data from the vendors table """
    #conn = None
    

    if(where != ""):
        where = ast.literal_eval(where)
        where_clause = ""
        for state, capital in where.items():
            where_clause += ((state + " = " + str(capital)) + ", ")

        where_clause = where_clause[:-2]

    final_selected = selected_item

    conn=psycopg2.connect(user = "postgres", password = "", host = "localhost",port = "5432", database = "postgres");


    try:
        #conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        if (where != ""):
            if(order_by != ""):
                cur.execute("SELECT " + final_selected + " FROM " +
                            table + " WHERE" +where_clause+ " ORDER BY " + order_by +";")
            else:
                cur.execute("SELECT " + final_selected + " FROM " +
                            table + " WHERE " +where_clause + ";")
        else:
            cur.execute("SELECT " + final_selected + " FROM " +
                            table + ";")

        print("The number of parts: ", cur.rowcount)
        """fecth all data from selection"""
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#python3.7 main_backend.py -c update -t "user" FirstName=\'win\' UserID=2
def update_table(table, set_key, pri_key_condition):
    conn=psycopg2.connect(user = "postgres", password = "", host = "localhost",port = "5432", database = "postgres");
    try:
        cursor = conn.cursor()

        # Update single record now
        sql_update_query = ("""Update %s set %s where %s;"""% (table, set_key, pri_key_condition))
        print(sql_update_query)
        cursor.execute(sql_update_query)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
        print("Table After updating record ")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
    finally:
        # closing database connection.
        if (conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

#main_backend.py -c delete -t user userid=1
def delete_data(table, where_clause = ""):
    """ delete part by part id """
    conn=psycopg2.connect(user = "postgres", password = "", host = "localhost",port = "5432", database = "postgres");
    cur = conn.cursor()
    rows_deleted = 0
    try:
        cur = conn.cursor()
        # execute the UPDATE  statement
        if(where_clause == ""):
            cur.execute("DELETE FROM %s;" % table);
        else:
            cur.execute("DELETE FROM %s WHERE %s;" % (table,where_clause));
        # get the number of updated rows
        rows_deleted = cur.rowcount
        print("Deleted %s rows from %s" % (rows_deleted,table));
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return rows_deleted


def main(argv):
    in_command = ''
    table = ''
    where_cmd = ''
    orderby_cmd = ''
    select_tuple = '*'
    arg_list = sys.argv[1:];

    try:
        opts, args = getopt.getopt(argv,"hc:t:w:o:s:",["command=","table=", "where=", "orderby=","select_tuple="])
        
    except getopt.GetoptError:
        print ('main_backend.py -c <sql_command> -t <tablename> <agr1> <arg2> ...')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('main_backend.py -c <sql_command> -t <tablename> <agr1> <arg2> ...')
            print ('main_backend.py -c insert -t <tablename> <attr1,attr2,attr3...>')
            print ('main_backend.py -c select -t <tablename> ....select all')
            print ('main_backend.py -c select -t <tablename> <attr1,attr2..> <where_condition> <order_by> ....select with condition')
            print ('main_backend.py -c update -t <tablename> <key> <new_value> ....update')
            print ('main_backend.py -c delete -t <tablename> <key> ....delete all records')
            print ('main_backend.py -c delete -t <tablename> <key> <where_clause> ....delete conditional entires')
            sys.exit()
        elif opt in ("-c", "--command"):
            in_command = arg
        elif opt in ("-t", "--table"):
            table = arg
            if(table == "user"):
                table = "\"user\""
        elif opt in ("-w", "--where"): 
            where_cmd = arg
        elif opt in ("-o", "--orderby"):
            orderby_cmd = arg
        elif opt in ("-s", "--select_tuple"):
            select_tuple = arg
    
    #print(arg_list[2]);
    if(in_command == "insert"):    
        insert_data(table, arg_list[4]);
    elif (in_command == "select"):
        if(False):
            if (len(arg_list) == 4):
                select_all_where(table);
            elif (len(arg_list) == 5):
                select_all_where(table, arg_list[5]);
            elif (len(arg_list) == 6):
                select_all_where(table, arg_list[5], arg_list[6]);
            elif (len(arg_list) == 7):
                select_all_where(table, arg_list[5], arg_list[6], arg_list[7]);
            else:
                print ("too many arguments - select");
        select_all_where(table, select_tuple, where_cmd, orderby_cmd);
    elif (in_command == "update"):
        update_table(table,arg_list[4], arg_list[5]);
    elif (in_command == 'delete'):
        if (len(arg_list) == 4):
            delete_data(table)
        elif (len(arg_list) == 5):
            delete_data(table, arg_list[4]);
        else:
            print("too many arguments - delete")



   # cmd_option = {"select" : insert_data(),
    #        "update" : sql_flower,
     #       "delete" : sql_music,
      #      "insert" : sql_food,
    #}

if __name__ == "__main__":
   main(sys.argv[1:])








