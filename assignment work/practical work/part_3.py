#!/usr/bin/python
import sqlite3
db = sqlite3.connect('./db/orinoco.db', isolation_level= None)
def _display_options(all_options,title,type):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    for option in all_options:
        code = option[0]
        desc = option[1]
        print("{0}.\t{1}".format(option_num, desc))
        option_num = option_num + 1
        option_list.append(code)
    global selected_option                          #i changed selected_option to be global, whilst a lazy fix, it did make calling it's result no matter where i was far simpler.
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+type+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]

    
    
def _display_3_options(all_options,title,type):    #modified the given function for ease of use in the seller select screen for menu option 2
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    for option in all_options:
        code = option[0]
        desc = option[1]
        desc2 = option[2]
        desc3 = option[3]
        print("{0}.\t{1}\t{2}\t{3}".format(option_num, desc, desc2, desc3))
        option_num = option_num + 1
        option_list.append(code)
    global selected_option
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+type+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]

order_get ="SELECT IFNULL(op.order_id,'empty'), \
            STRFTIME('%d-%m-%Y',so.order_date),\
            p.product_description,\
            s.seller_name,\
            op.price,\
            op.quantity,\
            so.order_status\
            FROM ordered_products op \
            INNER JOIN\
            shopper_orders so ON op.order_id = so.order_id\
            INNER JOIN\
            products p ON op.product_id = p.product_id\
            INNER JOIN\
            sellers s ON s.seller_id = op.seller_id\
            WHERE shopper_id = (?)\
            ORDER BY so.order_date DESC"                         # the SQLite query to retrieve the list of orders, given a shopper ID

prod_get =  'SELECT product_id, \
            product_description \
            FROM products \
            WHERE category_id = (?)'                             # retrieves a list of products that match the provided category ID, taken from the _display_options function using the global selected_option

cat_get = 'SELECT category_id,\
           category_description\
            FROM categories'                                     # retrieves a list of categories, for use with the _display_options function

seller_get ="SELECT ps.product_id\
            ,s.seller_name\
            ,ps.price\
            ,s.seller_id\
            FROM product_sellers ps\
                 INNER JOIN\
            sellers s ON s.seller_id = ps.seller_id\
            WHERE product_id = (?); "                            # retrieves a list of vendors who sell a given product, once supplied the product ID, taken from the _display_options function 

basket_add_confirm ='SELECT ps.seller_id\
                ,s.seller_name\
                ,p.product_description\
                ,ps.price\
                FROM product_sellers ps\
                    INNER JOIN\
                sellers s ON s.seller_id = ps.seller_id\
                    INNER JOIN\
                products p ON p.product_id = ps.product_id\
                WHERE ps.product_id = ?\
                AND ps.seller_id = ?'                            # retrives the relevant information for an item about to be added to the basket

basket_add = "INSERT INTO shopper_baskets (shopper_id,basket_created_date_time)\
                VALUES(?,CURRENT_DATE);"                                                 #inserts the necessary row into the shopper_baskets table, to facilitate later items to be added to it.

purchase_product = "INSERT INTO basket_contents (basket_id,product_id,seller_id,quantity,price)\
                    VALUES(?,?,?,?,?)"                                                   #inserts necessary rows into basket_contents, when the customer adds an item to basket

view_basket = "SELECT p.product_description,\
                      s.seller_name,\
                      ps.seller_id,\
                      bc.quantity,\
                      bc.price\
               FROM basket_contents bc\
                        INNER JOIN\
                products p ON p.product_id = bc.product_id\
                        INNER JOIN\
                product_sellers ps ON ps.product_id = bc.product_id\
                        INNER JOIN\
                sellers s ON s.seller_id = ps.seller_id\
                WHERE basket_id = ?"                                                    #retrieves the shoppers current basket, when provided a basket_id

total_price = "SELECT SUM(price*quantity)\
               FROM basket_contents\
               WHERE basket_id = ?"                                                     #provides a total price for a basket, when provided the basket_id
remove_from_basket = "DELETE FROM basket_contents\
                      WHERE basket_id = ?"                                             #removes basket contents from table, when provided a basket_id

remove_shopper_basket = "DELETE FROM shopper_baskets\
                         WHERE shopper_id = ?"                                         #removes shopper basket from table, when provided a shopper_id

loopval = 0              #loop values used to maintain a while loop through the menus, insuring continuity, without restarting the program.                                        
loopval2 = 0

print ("\n")
while loopval == 0:
    cursor = db.cursor()                            #creating a cursor object 
    shopper_id = input("enter your shopper ID number: ")       
    
    if shopper_id.isdigit():                  #ensuring an actual digit has been entered, as anything else will not work.
        
        print('ORINOCO - SHOPPER MAIN MENU\
            \n_______________________________________________\
             \n1.Display your order history \
             \n2.add an item to your basket \
             \n3.view your basket \
			 \n4.Change the quantity of an item in your basket\
			 \n5.Remove an item from your basket\
             \n6.checkout \
             \n7.exit')

        menu_input = input('select an option:')
        if menu_input == '1':
            cursor = db.cursor()
            cursor.execute(order_get,([shopper_id]))
            result = all_rows = cursor.fetchall()
            print('ORDER HISTORY \n _______________________________________________')
            print("     order ID   order date        product                 seller         price       quantity  order status\n") #an atrociously disorganised way of printing headings, however, they never occur again.

            for row in all_rows: #a for loop to print out each row, given that each query returns a list, with each position containing a "row" of the SQLite query. This prints these as such, formatting them afterward for readability.
                order_id = row[0]
                order_date = row[1]
                product_description = row[2]
                seller_name = row[3]
                price = row [4]
                quantity = row[5]
                order_status = row[6]
                print("{0:12}\t{1:}\t{2:18}\t{3:14}\t£{4:7.2f}\t{5:2}\t{6:12}".format(order_id, order_date[:10], product_description[:15], seller_name[:14], price, \
                quantity, order_status[:8]))
                                                                                                          

            leavemenu = input("return to main menu? if you select no, the program will terminate(y/n)") #a simple input prompt to ask the user to decide to continue or not.
            if leavemenu == 'y':
                loopval = 0
            elif leavemenu == 'n':
                print('exiting program...')
                loopval = 1

        elif menu_input == '2':
            print('Add an item to your basket\n\n')
            cursor.execute(basket_add,[shopper_id]) #The transaction that adds a basket to the shopper_basket table in the database, passed the shopper ID given by the user earlier.
            print('basket successfully created')
            loopval2 = 0
            while loopval2 == 0:
                    cursor.execute(cat_get)
                    all_rows = cursor.fetchall()
                    _display_options(all_rows,'categories','number')
                    
                    selected_category = str(selected_option)       #SQLite queries could only be parsed as strings, otherwise it would take up too many bindings. using 'str()' to format the result as a string, results in it only taking up a single binding.
                    cursor.execute(prod_get,selected_category)
                    all_rows = cursor.fetchall()
                    _display_options(all_rows,'products','number')        #usage of the _display_options function.
                    first = []                                    
                    for a_tuple in all_rows:                              #from line 208, to line 213, is an example of a method for attaining only the first element from a tuple, from a list. in this case, all_rows.
                        first.append(a_tuple[0])
                    
                    selected_product = ((first[(selected_option-1)]))
                    selected_product_id = str(selected_product)
                    cursor.execute(seller_get,[selected_product_id])
                    all_rows = cursor.fetchall()
                    _display_3_options(all_rows,'sellers who sell this product','number')
                    first = []
                    for a_tuple in all_rows:
                        first.append(a_tuple[3])
                    selected_seller = ((first[(selected_option-1)]))
                    selected_seller_id = str(selected_seller)


                    cursor.execute(basket_add_confirm,((selected_product_id),(selected_seller_id)))
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        seller_id = row[0]
                        seller_name = row[1]
                        product_description =row[2]
                        price = row[3]
                        print("{0}\t{1}\t{2}\t{3}".format(seller_id,seller_name,product_description,price))
                    purchase_quantity = input("enter a quantity to buy: ")
                    
                    if purchase_quantity.isdigit:                   #double checking that the input quantity is, in fact, a digit
                        cursor.execute("SELECT basket_id FROM shopper_baskets WHERE shopper_id = ?",[shopper_id])      #instead of making this a called function, i opted to do it as is, since i only use it once and it can occupy one line.
                        all_rows = cursor.fetchall()
                        first = []
                        for a_tuple in all_rows:
                            first.append(a_tuple[0])
                        basket_id_tuple = first[0]
                        basket_id = str(basket_id_tuple)
                        cursor.execute("SELECT price FROM product_sellers WHERE product_id = ? AND seller_id = ?",((selected_product_id),(selected_seller_id)))
                        all_rows = cursor.fetchall()
                        first = []
                        for a_tuple in all_rows:
                            first.append(a_tuple[0])
                        price_tuple = first[0]
                        price = str(price_tuple)
                        add_confirm = input("add item to basket? (y/n)")
                        if add_confirm == 'y':                                        #if the shopper confirms, then it will notify the shopper, if no is selected, it will inform them of the cancellation
                            cursor.execute(purchase_product,((basket_id),(selected_product_id),(selected_seller_id),purchase_quantity,(price)))  
                            print("successfully added to basket")
                        elif add_confirm =='n':
                            print("basket addition cancelled \n")
                            empty_basket = input("do you wish to empty your basket?(y/n)" )
                            if empty_basket == 'y':
                                cursor.execute(remove_shopper_basket,(shopper_id))
                                cursor.execute(remove_shopper_basket,[shopper_id])
                                db.commit()

                        exit_buy = input("do you wish to return to the main menu? (y/n)")
                        if exit_buy == 'y':
                            loopval2 = 1


                    else:
                        print("that was not a number, try again")
        
        elif menu_input == '3':
            print('\nCurrent Basket\n' + '_______________________________________________')
            cursor.execute("SELECT basket_id FROM shopper_baskets WHERE shopper_id = ?",[shopper_id])
            all_rows = cursor.fetchall()
            first = []
            for a_tuple in all_rows:
                first.append(a_tuple[0])
            first_tuple = first[0]
            basket_id_tuple = first_tuple
            basket_id = str(basket_id_tuple)
            cursor.execute(view_basket,[basket_id])
            all_rows = cursor.fetchall()
            print("basket contents:\n")
            for row in all_rows:
                    product_description = row[0]
                    seller_name = row[1]
                    seller_id =row[2]
                    quantity = row[3]
                    price = row[4]
                    print("{0}\t{1}\t{2}\t{3}\t{4}".format(product_description,seller_name,seller_id,quantity,price))

        elif menu_input == '6':
            print('checkout:\n_______________________________________________\nbasket:\n')
            cursor.execute("SELECT basket_id FROM shopper_baskets WHERE shopper_id = ?",[shopper_id])
            all_rows = cursor.fetchall()
            first = []
            for a_tuple in all_rows:
                first.append(a_tuple[0])
            basket_id_tuple = first[0]
            basket_id = str(basket_id_tuple)
            cursor.execute(view_basket,[basket_id])
            all_rows = cursor.fetchall()
            for row in all_rows:
                    product_description = row[0]
                    seller_name = row[1]
                    seller_id =row[2]
                    quantity = row[3]
                    price = row[4]
                    print("{0}\t{1}\t{2}\t{3}\t{4}".format(product_description,seller_name,seller_id,quantity,price))
            
            cursor.execute(total_price,[basket_id])
            all_rows = cursor.fetchall()
            first = []
            for a_tuple in all_rows:
                first.append(a_tuple[0])
            total_price_tuple = first[0]
            total_price = str(total_price_tuple)
            print("total price: £" + total_price)
            checkout_confirm = input("complete order? (y/n)")
            if checkout_confirm == 'y':
                confirm_order = input("confirm purchase? (y/n)")
                if confirm_order == 'y':
                    print("order placed successfully")
                    cursor.execute(remove_from_basket,[basket_id])
                    cursor.execute(remove_shopper_basket,[shopper_id])
                    db.commit()
                    leavemenu = input("return to main menu? if you select no, the program will terminate(y/n)")
                    if leavemenu == 'y':
                        loopval = 0
                    elif leavemenu == 'n':
                        print('exiting program...')
                        loopval = 1
        elif menu_input == '7':
            loopval =                   1
            db.close()
            print('exiting program...')

        else:
            print("entered value is not numerical, please try again")