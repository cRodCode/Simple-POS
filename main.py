# Project:  SimplePOS
# Author:   Carlos Rodriguez-Malak
# Date:     March 10, 2024
# Purpose:  Create a Simple Point of Sell System
#           With Clear to read options
#           and easy access to funtions


import stripe
import customtkinter
from tkinter import messagebox
import bcrypt


class App(customtkinter.CTk, ):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("SimplePOS")
        self.all_main_objects = []
        self.all_login_objects = []
        self.logs = []
        self.total = float(0.00)
        self.tax = float(self.total*.08375)
        self.grand_total = float(self.tax + self.total)
        self.stripe_api_key = "ENTER STRIPE API KEY HERE"
        self.custom_font = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold", slant="italic")
        self.user = "no_user"   # Default to no_user
        self.orderID = ""       # Order ID
        self.admin = False      # Default to not admin

        # Create labels, entry widgets, and buttons for the login screen
        self.login_screen()

    def login_screen(self):
        # Clear the screen and display the login widgets
        self.move_all_items()
        self.username_label = customtkinter.CTkLabel(self, text="Username:")
        self.username_label.place(x=420, y=250)
        self.all_login_objects.append(self.username_label)
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.place(x=500, y=250)
        #self.username_entry.focus()
        self.all_login_objects.append(self.username_entry)
        self.password_label = customtkinter.CTkLabel(self, text="Password:")
        self.password_label.place(x=420, y=300)
        self.all_login_objects.append(self.password_label)
        self.password_entry = customtkinter.CTkEntry(self, show="*")  # show="*" hides the entered characters
        self.password_entry.place(x=500, y=300)
        self.password_entry.bind('<Return>', command=self.activate_button)
        self.all_login_objects.append(self.password_entry)
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.handle_login, font=self.custom_font)
        self.login_button.place(x=435, y=400)

        self.all_login_objects.append(self.login_button)

    def activate_button(self, string):
        self.handle_login()

    def main_screen(self):
        # Clear the screen and display the main screen widgets
        self.move_all_items()
        self.clear_screen()

        # Add widgets to the main screen How to default main layout will be
        self.scrollable_item_list = customtkinter.CTkTextbox(self, width=300, height=250, border_width=1, fg_color="black", text_color="white", font=self.custom_font, state="normal")
        self.scrollable_item_list.place(x=700,y=0)

        self.button1 = customtkinter.CTkButton(self, text='Medium Pizza 12"', command=self.button_click1, height=100, font=self.custom_font, border_width=2)
        self.button1.place(x=0, y=0)
        self.button2 = customtkinter.CTkButton(self, text='Large Pizza 14"', command=self.button_click2, height=100, font=self.custom_font, border_width=2)
        self.button2.place(x=140, y=0)
        self.button3 = customtkinter.CTkButton(self, text='X Large Pizza 16"', command=self.button_click3, height=100, font=self.custom_font, border_width=2)
        self.button3.place(x=280, y=0)
        self.button4 = customtkinter.CTkButton(self, text='Cheese\nCalzone\n$11.95', command=self.button_click4, height=100, font=self.custom_font, border_width=2)
        self.button4.place(x=420, y=0)
        self.button5 = customtkinter.CTkButton(self, text='New York\nStromboli\n$11.95', command=self.button_click5, height=100, font=self.custom_font, border_width=2)
        self.button5.place(x=0, y=100)
        self.button6 = customtkinter.CTkButton(self, text='Veggies\nStromboli\n$13.95', command=self.button_click6, height=100, font=self.custom_font, border_width=2)
        self.button6.place(x=140, y=100)
        self.button7 = customtkinter.CTkButton(self, text='Chicken Wings\n(8 pc)\n$13.95', command=self.button_click7, height=100, font=self.custom_font, border_width=2)
        self.button7.place(x=280, y=100)
        self.button8 = customtkinter.CTkButton(self, text='Chicken Wings\n(12 pc)\n$16.95', command=self.button_click8, height=100, font=self.custom_font, border_width=2)
        self.button8.place(x=420, y=100)
        self.back_btn = customtkinter.CTkButton(self, text='BACK', command=self.btn_back_clicked, height=100, font=self.custom_font, border_width=2)
        self.back_btn.place(x=560, y=300)
        self.button10 = customtkinter.CTkButton(self, text='Pretzel Pizza\nCheese Only\n$7.99', command=self.button_click10, height=100, font=self.custom_font, border_width=2)
        self.button10.place(x=0, y=200)
        self.button11 = customtkinter.CTkButton(self, text='Pretzel Pizza\nCheese & Pepperoni\n$8.99', command=self.button_click11, height=100, font=self.custom_font, border_width=2)
        self.button11.place(x=140, y=200)
        self.button12 = customtkinter.CTkButton(self, text='Pretzel Roll\n(1 pc)\n$4.99', command=self.button_click12, height=100, font=self.custom_font, border_width=2)
        self.button12.place(x=280, y=200)
        self.button13 = customtkinter.CTkButton(self, text='Tater Tots\n(10 pc)\n$5.99', command=self.button_click13, height=100, font=self.custom_font, border_width=2)
        self.button13.place(x=420, y=200)
        self.button14 = customtkinter.CTkButton(self, text='Cheesecake\nPlain\n$4.99', command=self.button_click14, height=100, font=self.custom_font, border_width=2)
        self.button14.place(x=0, y=300)
        self.button15 = customtkinter.CTkButton(self, text='Cheesecake\nChocolate Drizzle\n$5.99', command=self.button_click15, height=100, font=self.custom_font, border_width=2)
        self.button15.place(x=140, y=300)
        self.button16 = customtkinter.CTkButton(self, text='CLEAR', command=self.button_click16, height=100, font=self.custom_font, border_width=2)
        self.button16.place(x=420, y=300)
        self.button17 = customtkinter.CTkButton(self, text='MISC', command=self.button_click17, height=100, font=self.custom_font, border_width=2)
        self.button17.place(x=280, y=300)
        self.button18 = customtkinter.CTkButton(self, text='CREATE USER', command=self.create_user, height=100, font=self.custom_font, border_width=2)
        self.button18.place(x=560, y=200)
        self.checkout_btn = customtkinter.CTkButton(self, text='CHECKOUT', command=self.checkout, height=100, font=self.custom_font, border_width=2)
        self.checkout_btn.place(x=560, y=100)
        self.refund_btn = customtkinter.CTkButton(self, text='REFUND', command=self.refund, height=100, font=self.custom_font, border_width=2)
        self.refund_btn.place(x=560, y=0)

        #
        # LABELS
        #
        self.sub_total_lbl = customtkinter.CTkLabel(self, text="Sub Total\t\t   $0.00", fg_color="transparent", font=self.custom_font, text_color="green")
        self.sub_total_lbl.place(x=700, y=270)
        self.tax_lbl = customtkinter.CTkLabel(self, text="Tax\t\t\t   $0.00", fg_color="transparent", font=self.custom_font, text_color="green")
        self.tax_lbl.place(x=700, y=320)
        self.grand_total_lbl = customtkinter.CTkLabel(self, text="Grand Total\t\t   $0.00", fg_color="transparent", font=self.custom_font, text_color="green")
        self.grand_total_lbl.place(x=700, y=370)
        self.user_lbl = customtkinter.CTkLabel(self, text=self.user.upper(), fg_color="transparent", font=self.custom_font)
        self.user_lbl.place(x=850, y=570)


        #
        # ALL MEDIUM PIZZAS
        #
        self.button_med_pizza1 = customtkinter.CTkButton(self, text='Cosa\nNostra\n$16.95', command=self.button_med_pizza1, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza2 = customtkinter.CTkButton(self, text='Bianca\n$16.95', command=self.button_med_pizza2, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza3 = customtkinter.CTkButton(self, text='Clam\nCasino\n$16.95', command=self.button_med_pizza3, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza4 = customtkinter.CTkButton(self, text='Hawaiian\n$14.95', command=self.button_med_pizza4, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza5 = customtkinter.CTkButton(self, text='California\n$16.95', command=self.button_med_pizza5, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza6 = customtkinter.CTkButton(self, text='Pesto\n$16.95', command=self.button_med_pizza6, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza7 = customtkinter.CTkButton(self, text='Louisiana\n$16.95', command=self.button_med_pizza7, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza8 = customtkinter.CTkButton(self, text='Napoli\n$16.95', command=self.button_med_pizza8, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza9 = customtkinter.CTkButton(self, text='Quattro\nStagioni\n$16.95', command=self.button_med_pizza9, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza10 = customtkinter.CTkButton(self, text='Mozzarella\n$10.95', command=self.button_med_pizza10, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza11 = customtkinter.CTkButton(self, text='New York\nSpecial\n$16.95', command=self.button_med_pizza11, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza12 = customtkinter.CTkButton(self, text='Vegetarian\nSpecial\n$16.95', command=self.button_med_pizza12, height=100, font=self.custom_font, border_width=2)
        self.button_med_pizza13 = customtkinter.CTkButton(self, text='Meat\nLovers\n$16.95', command=self.button_med_pizza13, height=100, font=self.custom_font, border_width=2)

        #
        # ALL LARGE PIZZAS
        #
        self.button_lrg_pizza1 = customtkinter.CTkButton(self, text='Cosa\nNostra\n$18.95', command=self.button_lrg_pizza1, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza2 = customtkinter.CTkButton(self, text='Bianca\n$18.95', command=self.button_lrg_pizza2, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza3 = customtkinter.CTkButton(self, text='Clam\nCasino\n$18.95', command=self.button_lrg_pizza3, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza4 = customtkinter.CTkButton(self, text='Hawaiian\n$18.95', command=self.button_lrg_pizza4, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza5 = customtkinter.CTkButton(self, text='California\n$18.95', command=self.button_lrg_pizza5, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza6 = customtkinter.CTkButton(self, text='Pesto\n$18.95', command=self.button_lrg_pizza6, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza7 = customtkinter.CTkButton(self, text='Louisiana\n$18.95', command=self.button_lrg_pizza7, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza8 = customtkinter.CTkButton(self, text='Napoli\n$18.95', command=self.button_lrg_pizza8, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza9 = customtkinter.CTkButton(self, text='Quattro\nStagioni\n$18.95', command=self.button_lrg_pizza9, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza10 = customtkinter.CTkButton(self, text='Mozzarella\n$11.95', command=self.button_lrg_pizza10, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza11 = customtkinter.CTkButton(self, text='New York\nSpecial\n$18.95', command=self.button_lrg_pizza11, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza12 = customtkinter.CTkButton(self, text='Vegetarian\nSpecial\n$18.95', command=self.button_lrg_pizza12, height=100, font=self.custom_font, border_width=2)
        self.button_lrg_pizza13 = customtkinter.CTkButton(self, text='Meat\nLovers\n$18.95', command=self.button_lrg_pizza13, height=100, font=self.custom_font, border_width=2)

        #
        # ALL X-LARGE PIZZAS
        #
        self.button_xlrg_pizza1 = customtkinter.CTkButton(self, text='Cosa\nNostra\n$21.95', command=self.button_xlrg_pizza1, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza2 = customtkinter.CTkButton(self, text='Bianca\n$21.95', command=self.button_xlrg_pizza2, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza3 = customtkinter.CTkButton(self, text='Clam\nCasino\n$21.95', command=self.button_xlrg_pizza3, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza4 = customtkinter.CTkButton(self, text='Hawaiian\n$19.95', command=self.button_xlrg_pizza4, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza5 = customtkinter.CTkButton(self, text='California\n$21.95', command=self.button_xlrg_pizza5, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza6 = customtkinter.CTkButton(self, text='Pesto\n$21.95', command=self.button_xlrg_pizza6, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza7 = customtkinter.CTkButton(self, text='Louisiana\n$21.95', command=self.button_xlrg_pizza7, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza8 = customtkinter.CTkButton(self, text='Napoli\n$21.95', command=self.button_xlrg_pizza8, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza9 = customtkinter.CTkButton(self, text='Quattro\nStagioni\n$21.95', command=self.button_xlrg_pizza9, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza10 = customtkinter.CTkButton(self, text='Mozzarella\n$17.95', command=self.button_xlrg_pizza10, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza11 = customtkinter.CTkButton(self, text='New York\nSpecial\n$21.95', command=self.button_xlrg_pizza11, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza12 = customtkinter.CTkButton(self, text='Vegetarian\nSpecial\n$21.95', command=self.button_xlrg_pizza12, height=100, font=self.custom_font, border_width=2)
        self.button_xlrg_pizza13 = customtkinter.CTkButton(self, text='Meat\nLovers\n$21.95', command=self.button_xlrg_pizza13, height=100, font=self.custom_font, border_width=2)


        self.all_main_objects.append(self.button1)
        self.all_main_objects.append(self.button2)
        self.all_main_objects.append(self.button3)
        self.all_main_objects.append(self.button4)
        self.all_main_objects.append(self.button5)
        self.all_main_objects.append(self.button6)
        self.all_main_objects.append(self.button7)
        self.all_main_objects.append(self.button8)
        self.all_main_objects.append(self.button10)
        self.all_main_objects.append(self.button11)
        self.all_main_objects.append(self.button12)
        self.all_main_objects.append(self.button13)
        self.all_main_objects.append(self.button14)
        self.all_main_objects.append(self.button15)
        self.all_main_objects.append(self.checkout_btn)
        self.all_main_objects.append(self.back_btn)
        self.all_main_objects.append(self.button_med_pizza1)
        self.all_main_objects.append(self.button_med_pizza2)
        self.all_main_objects.append(self.button_med_pizza3)
        self.all_main_objects.append(self.button_med_pizza4)
        self.all_main_objects.append(self.button_med_pizza5)
        self.all_main_objects.append(self.button_med_pizza6)
        self.all_main_objects.append(self.button_med_pizza7)
        self.all_main_objects.append(self.button_med_pizza8)
        self.all_main_objects.append(self.button_med_pizza9)
        self.all_main_objects.append(self.button_med_pizza10)
        self.all_main_objects.append(self.button_med_pizza11)
        self.all_main_objects.append(self.button_med_pizza12)
        self.all_main_objects.append(self.button_med_pizza13)
        self.all_main_objects.append(self.button_lrg_pizza1)
        self.all_main_objects.append(self.button_lrg_pizza2)
        self.all_main_objects.append(self.button_lrg_pizza3)
        self.all_main_objects.append(self.button_lrg_pizza4)
        self.all_main_objects.append(self.button_lrg_pizza5)
        self.all_main_objects.append(self.button_lrg_pizza6)
        self.all_main_objects.append(self.button_lrg_pizza7)
        self.all_main_objects.append(self.button_lrg_pizza8)
        self.all_main_objects.append(self.button_lrg_pizza9)
        self.all_main_objects.append(self.button_lrg_pizza10)
        self.all_main_objects.append(self.button_lrg_pizza11)
        self.all_main_objects.append(self.button_lrg_pizza12)
        self.all_main_objects.append(self.button_lrg_pizza13)
        self.all_main_objects.append(self.button_xlrg_pizza1)
        self.all_main_objects.append(self.button_xlrg_pizza2)
        self.all_main_objects.append(self.button_xlrg_pizza3)
        self.all_main_objects.append(self.button_xlrg_pizza4)
        self.all_main_objects.append(self.button_xlrg_pizza5)
        self.all_main_objects.append(self.button_xlrg_pizza6)
        self.all_main_objects.append(self.button_xlrg_pizza7)
        self.all_main_objects.append(self.button_xlrg_pizza8)
        self.all_main_objects.append(self.button_xlrg_pizza9)
        self.all_main_objects.append(self.button_xlrg_pizza10)
        self.all_main_objects.append(self.button_xlrg_pizza11)
        self.all_main_objects.append(self.button_xlrg_pizza12)
        self.all_main_objects.append(self.button_xlrg_pizza13)

    # add methods to app
    def button_click1(self):                    # medium pizza
        self.move_all_items()                   # move all items offscreen
        self.back_btn.place(x=560, y=300)
        self.move_all_med_pizzas()
    #   Move all medium pizza option onto screem
    def button_click2(self):                    # large pizza
        self.move_all_items()                   # move all items offscreen
        self.back_btn.place(x=560, y=300)
        self.move_all_lrg_pizzas()
    def button_click3(self):                    # x large pizza
        self.move_all_items()                   # move all items offscreen
        self.back_btn.place(x=560, y=300)
        self.move_all_xlrg_pizzas()

    def button_click4(self):
        self.update_total(float(11.95))

        self.scrollable_item_list.insert("0.0", "Cheese Calzone $11.95\n")
    def button_click5(self):
        self.scrollable_item_list.insert("0.0", "New York Stromboli $11.95\n")
        self.update_total(float(11.95))
    def button_click6(self):
        self.scrollable_item_list.insert("0.0", "Veggies Stromboli $13.95\n")
        self.update_total(float(13.95))
    def button_click7(self):
        self.scrollable_item_list.insert("0.0", "Chicken Wings (8 pc) $13.95\n")
        self.update_total(float(13.95))
    def button_click8(self):
        self.scrollable_item_list.insert("0.0", "Chicken Wings (12 pc) $16.95\n")
        self.update_total(float(16.95))
    def btn_back_clicked(self):            # BACK BUTTON
        self.move_all_items()
        self.main_screen_layout()
    def button_click10(self):
        self.scrollable_item_list.insert("0.0", "Pretzel Pizza Cheese Only $7.99\n")
        self.update_total(float(7.99))
    def button_click11(self):
        self.scrollable_item_list.insert("0.0", "Pretzel Pizza Cheese & Pepperoni $8.99\n")
        self.update_total(float(8.99))
    def button_click12(self):
        self.scrollable_item_list.insert("0.0", "Pretzel Roll (1 pc) $4.99\n")
        self.update_total(float(4.99))
    def button_click13(self):
        self.scrollable_item_list.insert("0.0", "Tater Tots (10 pc) $5.99\n")
        self.update_total(float(5.99))
    def button_click14(self):
        self.scrollable_item_list.insert("0.0", "Cheesecake Plain $4.99\n")
        self.update_total(float(4.99))
    def button_click15(self):
        self.scrollable_item_list.insert("0.0", "Cheesecake Chocolate Drizzle $5.99\n")
        self.update_total(float(5.99))
    def button_click16(self):
        self.clear_total()
        self.scrollable_item_list.delete(1.0, 'end')

    def button_click17(self):
        self.misc_price()

    ##
    ##  ALL MEDIUM PIZZAS
    ##
    def button_med_pizza1(self):        
        self.scrollable_item_list.insert("0.0", "Cosa Nostra $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza2(self):
        self.scrollable_item_list.insert("0.0", "Bianca $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza3(self):
        self.scrollable_item_list.insert("0.0", "Clam Casino $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza4(self):
        self.scrollable_item_list.insert("0.0", "Hawaiian $16.95\n")
        self.update_total(float(14.95))
    def button_med_pizza5(self):
        self.scrollable_item_list.insert("0.0", "California $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza6(self):
        self.scrollable_item_list.insert("0.0", "Pesto $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza7(self):
        self.scrollable_item_list.insert("0.0", "Louisiana $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza8(self):
        self.scrollable_item_list.insert("0.0", "Napoli $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza9(self):
        self.scrollable_item_list.insert("0.0", "Quattro Stagioni $16.95\n")
        self.update_total(float(16.95))
    def button_med_pizza10(self):
        self.update_total(float(10.95))
        self.scrollable_item_list.insert("0.0", "Mozzarella $10.95\n")
    def button_med_pizza11(self):
        self.update_total(float(16.95))
        self.scrollable_item_list.insert("0.0", "New York Special $16.95\n")
    def button_med_pizza12(self):
        self.update_total(float(16.95))
        self.scrollable_item_list.insert("0.0", "Vegetarian Special $16.95\n")
    def button_med_pizza13(self):
        self.update_total(float(10.95))
        self.scrollable_item_list.insert("0.0", "Meat Lovers $16.95\n")


    ##
    ##  ALL LARGE PIZZAS
    ##
    def button_lrg_pizza1(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Meat Lovers $18.95\n")
    def button_lrg_pizza2(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Bianca $18.95\n")

    def button_lrg_pizza3(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Clam Casino $18.95\n")

    def button_lrg_pizza4(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Hawaiian $18.95\n")

    def button_lrg_pizza5(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "California $18.95\n")

    def button_lrg_pizza6(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Pesto $18.95\n")

    def button_lrg_pizza7(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Louisiana $18.95\n")

    def button_lrg_pizza8(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Napoli $18.95\n")

    def button_lrg_pizza9(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Quattro Stagioni $18.95\n")

    def button_lrg_pizza10(self):
        self.update_total(float(11.95))
        self.scrollable_item_list.insert("0.0", "Mozzarella $11.95\n")

    def button_lrg_pizza11(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "New York Special $18.95\n")

    def button_lrg_pizza12(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Vegetarian Special $18.95\n")

    def button_lrg_pizza13(self):
        self.update_total(float(18.95))
        self.scrollable_item_list.insert("0.0", "Meat Lovers $18.95\n")


    ##
    ##  ALL X-LARGE PIZZAS
    ##
    def button_xlrg_pizza1(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Cosa Nostra $21.95\n")

    def button_xlrg_pizza2(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Bianca $21.95\n")

    def button_xlrg_pizza3(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Clam Casino $21.95\n")

    def button_xlrg_pizza4(self):
        self.update_total(float(19.95))
        self.scrollable_item_list.insert("0.0", "Hawaiian $19.95\n")

    def button_xlrg_pizza5(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "California $21.95\n")

    def button_xlrg_pizza6(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Pesto $21.95\n")

    def button_xlrg_pizza7(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Louisiana $21.95\n")

    def button_xlrg_pizza8(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Napoli $21.95\n")

    def button_xlrg_pizza9(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Quattro Stagioni $21.95\n")

    def button_xlrg_pizza10(self):
        self.update_total(float(17.95))
        self.scrollable_item_list.insert("0.0", "Mozzarella $17.95\n")

    def button_xlrg_pizza11(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "New York Special $21.95\n")

    def button_xlrg_pizza12(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Vegetarian Special $21.95\n")

    def button_xlrg_pizza13(self):
        self.update_total(float(21.95))
        self.scrollable_item_list.insert("0.0", "Meat Lovers $21.95\n")

    def move_all_med_pizzas(self):
        self.button_med_pizza1.place(x=0, y=0)
        self.button_med_pizza2.place(x=140, y=0)
        self.button_med_pizza3.place(x=280, y=0)
        self.button_med_pizza4.place(x=420, y=0)
        self.button_med_pizza5.place(x=560, y=0)
        self.button_med_pizza6.place(x=0, y=100)
        self.button_med_pizza7.place(x=140, y=100)
        self.button_med_pizza8.place(x=280, y=100)
        self.button_med_pizza9.place(x=420, y=100)
        self.button_med_pizza10.place(x=560, y=100)
        self.button_med_pizza11.place(x=0, y=200)
        self.button_med_pizza12.place(x=140, y=200)
        self.button_med_pizza13.place(x=280, y=200)

    def move_all_lrg_pizzas(self):
        self.button_lrg_pizza1.place(x=0, y=0)
        self.button_lrg_pizza2.place(x=140, y=0)
        self.button_lrg_pizza3.place(x=280, y=0)
        self.button_lrg_pizza4.place(x=420, y=0)
        self.button_lrg_pizza5.place(x=560, y=0)
        self.button_lrg_pizza6.place(x=0, y=100)
        self.button_lrg_pizza7.place(x=140, y=100)
        self.button_lrg_pizza8.place(x=280, y=100)
        self.button_lrg_pizza9.place(x=420, y=100)
        self.button_lrg_pizza10.place(x=560, y=100)
        self.button_lrg_pizza11.place(x=0, y=200)
        self.button_lrg_pizza12.place(x=140, y=200)
        self.button_lrg_pizza13.place(x=280, y=200)
        
    def move_all_xlrg_pizzas(self):
        self.button_xlrg_pizza1.place(x=0, y=0)
        self.button_xlrg_pizza2.place(x=140, y=0)
        self.button_xlrg_pizza3.place(x=280, y=0)
        self.button_xlrg_pizza4.place(x=420, y=0)
        self.button_xlrg_pizza5.place(x=560, y=0)
        self.button_xlrg_pizza6.place(x=0, y=100)
        self.button_xlrg_pizza7.place(x=140, y=100)
        self.button_xlrg_pizza8.place(x=280, y=100)
        self.button_xlrg_pizza9.place(x=420, y=100)
        self.button_xlrg_pizza10.place(x=560, y=100)
        self.button_xlrg_pizza11.place(x=0, y=200)
        self.button_xlrg_pizza12.place(x=140, y=200)
        self.button_xlrg_pizza13.place(x=280, y=200)


    def main_screen_layout(self):
        self.button1.place(x=0, y=0)
        self.button2.place(x=140, y=0)
        self.button3.place(x=280, y=0)
        self.button4.place(x=420, y=0)
        self.button5.place(x=0, y=100)
        self.button6.place(x=140, y=100)
        self.button7.place(x=280, y=100)
        self.button8.place(x=420, y=100)
        self.back_btn.place(x=560, y=300)
        self.button10.place(x=0, y=200)
        self.button11.place(x=140, y=200)
        self.button12.place(x=280, y=200)
        self.button13.place(x=420, y=200)
        self.button14.place(x=0, y=300)
        self.button15.place(x=140, y=300)
        self.button16.place(x=420, y=300)
        self.button17.place(x=280, y=300)
        self.button18.place(x=560, y=200)
        self.checkout_btn.place(x=560, y=100)


    def update_total(self, newItem):
        self.total = round(self.total + newItem, 2)
        self.tax = round(self.total*.08375,2)
        self.grand_total = round(self.tax + self.total,2)
        self.sub_total_lbl.configure(text='Sub Total\t\t    $'+str(self.total), text_color="green")
        self.tax_lbl.configure(text='Tax\t\t\t    $'+str(self.tax), text_color="green")
        self.grand_total_lbl.configure(text='Grand Total\t\t    $'+str(self.grand_total), text_color="green")

    def move_all_items(self):
        for x in self.all_main_objects:
            x.place(x=-500, y=0)

    def clear_total(self):
        self.total = 0.00
        self.update_total(0.00)

    def misc_price(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
        text = dialog.get_input()  # waits for input
        try:
            self.update_total(float(text))
            self.scrollable_item_list.insert("0.0", "miscellaneous $" + text+"\n")
        except:
            messagebox.showerror("Invalid Input!", "Enter only numerical inputs!")

    #
    # CREATE NEW USER
    #
    def create_user(self):
        if self.admin:
            self.temp_widgets = []
            self.move_all_items()

            self.sub_total_lbl.place(x=-1000,y=0)
            self.button16.place(x=-1000, y=300)
            self.button17.place(x=-1000, y=300)
            self.button18.place(x=-1000, y=200)
            self.back_btn.place(x=-1000, y =0)
            usernamelbl = customtkinter.CTkLabel(self, text="Username", font=self.custom_font)
            usernamelbl.place(x=220, y=200)
            passwordlbl = customtkinter.CTkLabel(self, text="Password", font=self.custom_font)
            passwordlbl.place(x=220, y=250)
            self.username_create = customtkinter.CTkEntry(self, font=self.custom_font)
            self.username_create.place(x=300, y=200)
            self.password_create = customtkinter.CTkEntry(self, font=self.custom_font)
            self.password_create.place(x=300, y=250)
            self.createbtn = customtkinter.CTkButton(self, text='CREATE USER', command=self.add_user, height=100, font=self.custom_font)
            self.createbtn.place(x=420, y=300)
            self.cancel_btn = customtkinter.CTkButton(self, text='CANCEL', command=self.btn_cancel_clicked, height=100,font=self.custom_font)
            self.cancel_btn.place(x=560, y=300)
            self.temp_widgets.append(usernamelbl)
            self.temp_widgets.append(passwordlbl)
            self.temp_widgets.append(self.username_create)
            self.temp_widgets.append(self.password_create)
            self.temp_widgets.append(self.createbtn)
            self.temp_widgets.append(self.cancel_btn)
        else:
            messagebox.showerror(title="ADMIN ONLY", message="You do not have access to this feature! Requires admin privileges.")

    def btn_cancel_clicked(self):
        for widgets in self.temp_widgets:
            widgets.destroy()
        self.main_screen_layout()

    def add_user(self):
        try:
            # Hash a password
            hashed_password = bcrypt.hashpw(self.password_create.get().encode(), bcrypt.gensalt())
            # Open the file in binary mode and write the encrypted data
            with open("users.txt", mode="ab") as user_file:
                user_file.write("username:".encode() + self.username_create.get().encode() + "|password:".encode() + hashed_password + b"\n")
            user_file.close()
            messagebox.showinfo("User Created", "User {} created successfully!".format(self.username_create.get()))
        except Exception as e:
            print(e)
            messagebox.showerror("ERROR!", "Account not created. An error occurred!")

        for widgets in self.temp_widgets:
            widgets.destroy()
        self.main_screen_layout()

    #
    # LOGIN METHODS
    #
    def handle_login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if self.authenticate(entered_username, entered_password):
            messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
            self.main_screen()  # Transition to the main screen
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def authenticate(self, username, password):
        # Add your authentication logic here
        # For simplicity, this example considers "admin" as the valid username and "password" as the valid password
        users_file = open("users.txt", "r")
        for data in users_file.readlines():
            if bcrypt.checkpw(password.encode(), data[data.find("password:")+9:data.find("\n")].encode()) and data[data.find("username:")+9:data.find("|")] == username:
                self.user = username        # Keep track of which user is logged in
                return True
        users_file.close()
        if username == "admin" and password == "password":
            self.admin = True
            self.user = username
            return True
        else:
            return False

    def clear_screen(self):
        # Clear all widgets from the screen
        for widget in self.winfo_children():
            widget.destroy()


    def checkout(self):
        stripe.api_key = self.stripe_api_key
        stripe.api_version = "2023-10-16"
        try:
            amount = int(self.total*100)
            print(amount)
            current_charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Test POS Charge',
                source='tok_visa')
            self.orderID = current_charge.stripe_id
            self.writeLog()

            messagebox.showinfo(title="Payment Success!", message="Payment of $"+str(self.total)+" complete!")
            self.scrollable_item_list.delete(0, 'end')
            pass
        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught
            print('Status is: %s' % e.http_status)
            print('Code is: %s' % e.code)
            # param is '' in this case
            print('Param is: %s' % e.param)
            print('Message is: %s' % e.user_message)
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            print("Too many requests made to the API too quickly")
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            print("Invalid parameters were supplied to Stripe's API")
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            print("Authentication with Stripe's API failed")
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            print("Network communication with Stripe failed")
            pass
        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            print("Display a very generic error to the user, and maybe send yourself an email")
            pass


    def refund(self):
        stripe.api_key = self.stripe_api_key
        stripe.api_version = "2023-10-16"
        dialog = customtkinter.CTkInputDialog(text="Type in a orderID#:", title="Refund")
        text = dialog.get_input()  # waits for input

        try:
            refund = stripe.Refund.create(charge=str(text))
            self.orderID = refund.stripe_id
            self.total = refund.amount/100
            self.writeLog()
            messagebox.showinfo(title="Refund processed successfully:", message=str(refund))
            pass
        except stripe.error.StripeError as e:
            # Handle any Stripe API errors
            print("Error occurred while processing refund:", str(e))

    def writeLog(self):
        logs = open(file="logs.txt", mode='a')
        logs.write("ID#" + str(self.orderID) + ", TOTAL:$" + str(self.total) + ", USER:" + str(self.user) + "\n")


app = App()
app.mainloop()
