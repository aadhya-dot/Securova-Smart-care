import tkinter as tk
import speech_recognition as sr
import pyttsx3
from tkinter import PhotoImage, Text, Scrollbar, VERTICAL
from PIL import Image, ImageTk

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to capture user voice input
def get_voice_input():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        bot_response("Listening for your input...")
        root.update()
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            user_speech = recognizer.recognize_google(audio).lower()
            # bot_response(f"You said: {user_speech}")
            chat_box.tag_configure("user", foreground="blue" ,font=("Helvetica", 12))
            chat_box.insert(tk.END, f"\n  You said: {user_speech}","user")
            handle_input(user_speech)  # Process the voice input
        except sr.UnknownValueError:
            bot_response("Sorry, I didn't catch that. Could you please repeat?")
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            bot_response("Sorry, there seems to be a problem with the speech service.")
            speak("Sorry, there seems to be a problem with the speech service.")

# Function to handle user input and show appropriate responses
def handle_input(user_input):
    user_input = user_input.strip().lower()

    if user_input == "hello":
        bot_response("""Hello! Welcome to Securova Smart care, a one-stop solution for personalised care for all your service needs! 
                        How may I assist you  today?:   \n  1. New product \n  2. Customer support""")
        update_options(["1) New product", "2) Customer support"])
        speak("""Hello! How may i assist you today?: To know more or buy a New product, or Customer support""")
    elif user_input in option_mapping:
        handle_option(option_mapping[user_input])
    else:
        bot_response("I'm sorry, I didn't understand that. Please say 'Hello' to start.")
        speak("I'm sorry, I didn't understand that. Please say 'Hello' to start.")

# Function to display bot response in the chat box
def bot_response(response):
    chat_box.tag_configure("bold", font=("Arial", 12, "bold")) 
    chat_box.insert(tk.END, f"\n  Bot: {response}","bold")
    chat_box.see(tk.END)
    root.update()

# Function to update the options based on user selection
def update_options(options):
    for button in options_buttons:
        button.pack_forget()  # Hide all buttons initially

    for i, option in enumerate(options):
        if i < len(options_buttons):  # Ensure we don't exceed the button list
            options_buttons[i].config(text=option, command=lambda opt=option: handle_option(opt))
            row = i // 2  # Determine the row (0-indexed)
            column = i % 2  # Determine the column (0 or 1)
            options_buttons[i].grid(row=row, column=column, padx=5, pady=5, sticky='w')  # Show buttons in grid
            
    # for i, option in enumerate(options):
    #     if i < len(options_buttons):  # Ensure we don't exceed the button list
    #         options_buttons[i].config(text=option, command=lambda opt=option: handle_option(opt))
    #         options_buttons[i].pack(pady=2)  # Show only the relevant buttons

# Function to handle user option selection
def handle_option(option):
    if option == "1) New product":
        bot_response("Please select below which type of home security system you require")
        update_options(["Personal", "Home","Corporate"])
        root.update()
        speak("Good choice! Please select below which type of home security system you require.") 
        speak(" for personal use,  for home requirements , or for corporate use")
    elif option == "2) Customer support":
        bot_response("So what can i help you with today? Please select a category to proceed")
        update_options(["1) Troubleshooting an issue ", "2) Warranty and repair", "Speak to an representative"])
        root.update()
        speak("Great! So what can i help you with today? Please select a category below to proceed")
    elif option == "Personal":
        bot_response("Securova personal security system: \n1. Model Number: SH-SS2024 \n2. Availability: In Stock \n3. Camera Resolution: 1080p Full HD\n4. Field of View: 130 degrees \n5. Connectivity: Wi-Fi (2.4GHz & 5GHz) \n6. Power Source: Plug-in with a backup rechargeable battery")
        update_options(["1) Order Now", "2) Know more"])
        root.update()
        speak("Securova personal security system: Model Number: SH-SS2024. Please select one of the options below")
    elif option == "Home":
        bot_response("""Securova home security system: \n1. Model Number: SH-SS2024 \n2. Availability: In Stock \n3. Camera Resolution: 1080p Full HD\n4. Field of View: 130 degrees \n5. Connectivity: Wi-Fi (2.4GHz & 5GHz) \n6. Power Source: Plug-in with a backup rechargeable battery""")
        update_options(["1) Order Now", "2) Know more", "Back"])
        root.update()
        speak("Securova home security system: Model Number: SH-SS2024. Please select one of the options below")
    elif option == "Corporate":
        bot_response("Securova corporate security system: \n1. Model Number: SH-SS2024 \n2. Availability: In Stock \n3. Camera Resolution: 1080p Full HD\n4. Field of View: 130 degrees \n5. Connectivity: Wi-Fi (2.4GHz & 5GHz) \n6. Power Source: Plug-in with a backup rechargeable batter")
        update_options(["1) Order Now", "2) Know more"])
        root.update()
        speak("Securova corporate security system: Model Number: SH-SS2024. Please select one of the options below")
    #------------------------------------------------------------
    elif option == "1) Order Now":
        bot_response("Please select one of the pricing packages below:")
        update_options([" Basic package(2 camera, 1-year warranty)- ₹557", " Advanced package(4 camera, night vision, 2-year warranty)- ₹4,778", " Premium package(6 camera, night vision, motion detection, 3-year warranty)- ₹12,557", "cancel"])
        root.update()
        speak("Please select one of the pricing packages below")
#----------------------------------------------------------------------------------------------------------
    elif option == "2) Know more":
        bot_response("Tell me what do you want to know about?")
        update_options(["1) Pricing packages", "2) Availability", "3) Delivery options", "Close"])
        root.update()
        speak("Great! Tell me what do you want to know about?")
    elif option == "1) Pricing packages":
        bot_response("Pricing packages avilable are: \n1. Basic package(2 camera, 1-year warranty) \n2. Advanced package(4 camera, night vision, 2-year warranty) \n3. Premium package(6 camera, night vision, motion detection, 3-year warranty")
        update_options(["back", "Close"])
        root.update()
        speak("pricing packages avilable are ,1. Basic package(2 camera, 1-year warranty) ,2. Advanced package(4 camera, night vision, 2-year warranty) ,3. Premium package(6 camera, night vision, motion detection, 3-year warranty")
    elif option == "2) Availability":
        bot_response("The product is available only in Uttar pradesh, Madhya Pradesh and Delhi")
        update_options(["back", "Close"])
        root.update()
        speak("The product is available only in Uttar pradesh, Madhya Pradesh and Delhi")
    elif option == "3) Delivery options":
        bot_response("Following are the delivery options: \n1. Standard delivery(3-5 business days, free) \n2. Express deliveryc \n3. Same-day delivery(55rs) ")
        update_options(["back", "Close"])
        root.update()
        speak("Following are the delivery options ,1. Standard delivery(3-5 business days, free), 2. Express delivery(1-2 buisness days, 25rs), 3. Same-day delivery(55rs)")
#-------------------------------------------------------------------------------------------------------
    elif option == "1) Troubleshooting an issue ":
        bot_response("What issue are you facing?")
        update_options(["1) Connection issues", "2) Camera not working properly", "3) Mobile app issue", "Close"])
        root.update()
        speak("What issue are you facing??")
    elif option == "2) Warranty and repair":
        bot_response("Please select your suitable service")
        update_options(["1) Request a repair", "2) Request a replacement", "3) Check your warranty status", "Close"])
        root.update()
        speak("Please select your suitable service")
    elif option == "Speak to an representative":
        bot_response("Sure! you would be connected with a representative shortly")
        speak("Sure! you would be connected with a representative shortly regarding your issue")
        speak("Thank you for chatting! Have a great day!")
        root.quit()  # Close the application
        root.destroy()
#----------------------------------------------------------------------------------------------
    elif option == "1) Connection issues":
        bot_response("Please try checking \n1. if the network is working properly \n2. Restarting the camera \n3. check for WiFi signal strength")
        update_options(["Speak to an representative", "Close"])
        root.update()
        speak("Please try checking ,1. if the network is working properly ,2. Restarting the camera ,3. check for WiFi signal strength")
    elif option == "2) Camera not working properly":
        bot_response("I'm sorry your camera isn't working, Please try \n1. checking the indicator lights \n2. resetting the camera")
        update_options(["Speak to an representative", "Close"])
        root.update()
        speak("I'm sorry your camera isn't working, Please try ,1. checking the indicator lights ,2. resetting the camera")
    elif option == "3) Mobile app issue":
        bot_response("Please try \n1. check WiFi \n2. Restarting the app \n3. Reinstalling the app")
        update_options(["Speak to an representative", "Close"])
        root.update()
        speak("Please try ,1. check WiFi ,2. Restarting the app ,3. Reinstalling the app")
        #------------------------------------------------------------------------------------------------------
    elif option == "1) Request a repair":
        bot_response("Okay, your request has been registered an engineer will contact you shortly for confirming and scheduling the repair")
        update_options(["confirm", "cancel"])
        root.update()
        speak("Okay, your request has been registered an engineer will contact you shortly for confirming and scheduling the repair")
    elif option == "2) Request a replacement":
        bot_response("okay, your request has been registered and an engineer will contact you shortly for confirming and scheduling the replacement")
        update_options(["confirm", "cancel"])
        root.update()
        speak("Okay, your request has been registered an engineer will contact you shortly for confirming and scheduling the replacement")
    elif option == "3) Check your warranty status":
        bot_response("As per your registered account at our site you are eligible for the warranty till next 4 months")
        update_options(["Close","Back"])
        root.update()
        speak("As per your registered account at our site you are eligible for the warranty till next 4 months")
        #------------------------------------------------------------
    elif option in {" Basic package(2 camera, 1-year warranty)- ₹557"," Advanced package(4 camera, night vision, 2-year warranty)- ₹4,778"," Premium package(6 camera, night vision, motion detection, 3-year warranty)- ₹12,557"}:
        update_options([" Basic package(2 camera, 1-year warranty)- ₹557", " Advanced package(4 camera, night vision, 2-year warranty)- ₹4,778", " Premium package(6 camera, night vision, motion detection, 3-year warranty)- ₹12,557", "cancel"])
        bot_response("Please select your state from below to check if the product is available in your location for shipping")
        update_options(["1) Uttar Pradesh", "2) Delhi", "3) Madhya pradesh", "4) Not available in my location"])
        root.update()
        speak("Please select your state from below to check if the product is available in your location for shipping:")
    elif option in {"1) Uttar Pradesh","2) Delhi","3) Madhya pradesh"}:
        bot_response("Please select your preffered delivery option from below:")
        update_options(["1) Standard delivery(3-5 business days, free)", "2) Express delivery(1-2 buisness days, ₹25)", "3) Same-day delivery(₹55)", "cancel"])
        root.update()
        speak("Please select your preffered delivery option from below:")
    elif option in {"1) Standard delivery(3-5 business days, free)","2) Express delivery(1-2 buisness days, ₹25)","3) Same-day delivery(₹55)"}:
        bot_response("Thank you! Your order has been successfully registered, an engineer will contact you on your registered number at our site within 48 hours")
        update_options(["confirm", "cancel"])
        root.update()
        speak("Thank you! Your order has been successfully registered, an engineer will contact you on your registered number at our site within 48 hours")    
        #----------------------------------------------------------------------------------------
    elif option == "Back":
        bot_response("Back to main options. Please say 'Hello' to restart.")
        speak("Back to main options. Please say Hello to restart.")
    elif option == "back":
        bot_response("Tell me what do you want to know about?")
        update_options(["1) Pricing packages", "2) Availability", "3) Delivery options", "Close"])
        root.update()
        speak("Great! Tell me what do you want to know about?")
    elif option == "Close":
        bot_response("Thank you for chatting! Have a great day!")
        speak("Thank you for chatting! Have a great day!")
        root.quit()  # Close the application
        root.destroy()
    elif option in {"cancel","4) Not available in my location"}:
        bot_response("Your order has been cancelled. Thank you for chatting! Have a great day!")
        speak("Your order has been cancelled. Thank you for chatting! Have a great day!")
        root.quit()  # Close the application
        root.destroy()
    elif option == "confirm":
        bot_response("Your request has been confirmed. Thank you for chatting! Have a great day!")
        speak("Your order has been confirmed. Thank you for chatting! Have a great day!")
        root.quit()  # Close the application
        root.destroy()
    else:
        bot_response("I didn't understand that. Please try again.")
        speak("I didn't understand that. Please try again.")
        get_voice_input()  # After handling option, prompt again for voice input
    
# Create the main Tkinter window
root = tk.Tk()
root.title("Securova smartcare")
# root.configure(bg='grey')
root.state('zoomed')

# Load the image
background_image = Image.open(r"D:\jp_share\bg.png")  # Use the correct path to your image
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)  # Make it fill the window

header_label = tk.Label(root, text="Securova Smartcare, Customer Support Chat Bot: ", fg='black', font=("Arial", 12, "bold")) #bg='grey'
header_label.pack(pady=10)
header_label.place(x=150,y=5)

# Create a frame for the logo at the top
logo_frame = tk.Frame(root) #bg='grey'
logo_frame.pack(pady=10)
logo_frame.place(x=10, y=10)

# Load and display the logo
global logo_img  # Ensure the image object is global to avoid garbage collection
logo_img = PhotoImage(file=r"D:\jp_share\logo.png")  # Use the correct path to your image
logo_label = tk.Label(logo_frame, image=logo_img) #bg='grey'
logo_label.pack()

# ----------------------------

# cam1_frame = tk.Frame(root)
# cam1_frame.pack(pady=10)
# cam1_frame.place(x=10, y=50)

global cam1_img  # Ensure the image object is global to avoid garbage collection
cam1_img = PhotoImage(file=r"D:\jp_share\camm1.png")  # Use the correct path to your image
cam1_label = tk.Label(root, image=cam1_img,bg="white", borderwidth=0, width = 100, height=80)
cam1_label.pack()
cam1_label.place(x=10, y=130)

global cam2_img  # Ensure the image object is global to avoid garbage collection
cam2_img = PhotoImage(file=r"D:\jp_share\camm2.png")  # Use the correct path to your image
cam2_label = tk.Label(root, image=cam2_img, bg="white", borderwidth=0, width = 100, height=80)
cam2_label.pack()
cam2_label.place(x=10, y=210)

global cam3_img  # Ensure the image object is global to avoid garbage collection
cam3_img = PhotoImage(file=r"D:\jp_share\camm3.png")  # Use the correct path to your image
cam3_label = tk.Label(root, image=cam3_img, bg="white", borderwidth=0, width = 100, height=80)
cam3_label.pack()
cam3_label.place(x=10, y=290)

global cam4_img  # Ensure the image object is global to avoid garbage collection
cam4_img = PhotoImage(file=r"D:\jp_share\camm4.png")  # Use the correct path to your image
cam4_label = tk.Label(root, image=cam4_img, bg="white", borderwidth=0, width = 100, height=112)
cam4_label.pack()
cam4_label.place(x=10, y=370)

global cam5_img  # Ensure the image object is global to avoid garbage collection
cam5_img = PhotoImage(file=r"D:\jp_share\camm5.png")  # Use the correct path to your image
cam5_label = tk.Label(root, image=cam5_img, bg="white", borderwidth=0, width = 100, height=80)
cam5_label.pack()
cam5_label.place(x=10, y=482)

global cam6_img  # Ensure the image object is global to avoid garbage collection
cam6_img = PhotoImage(file=r"D:\jp_share\camm6.png")  # Use the correct path to your image
cam6_label = tk.Label(root, image=cam6_img, bg="white", borderwidth=0, width = 100, height=80)
cam6_label.pack()
cam6_label.place(x=10, y=562)
# ----------------------------







# Create a frame for the chat box
chat_frame = tk.Frame(root, width=520 , height=650) #bg='grey'
chat_frame.pack(pady=10, padx=10)
chat_frame.place(x=115,y=35)

# Create a chat box with scroll
chat_box = Text(chat_frame, height=25, width=135, wrap="word", bg='white') 
chat_box.tag_configure("Bot", foreground="blue")
chat_box.tag_configure("user", foreground="green")
chat_box.pack(side=tk.LEFT, padx=15, pady=25, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(chat_frame, orient=VERTICAL, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

# Button to trigger voice input
# Load the microphone image
# Create a canvas for circular button
#canvas = tk.Canvas(root, width=100, height=100, bg='white', highlightthickness=0)
#canvas.pack(pady=20)

# Draw a circular shape
#canvas.create_oval(10, 10, 90, 90, fill='white', outline='black')  # Adjust as needed for size
microphone_img = PhotoImage(file=r"D:\jp_share\mic.png")  # Update the path to your image

# Create the Speak button with the image
voice_button = tk.Button(root, text="", command=get_voice_input, fg="white", font=("Arial", 14), #bg="grey"
                         image=microphone_img, compound=tk.RIGHT)  # compound=tk.LEFT places the image on the left

# voice_button = tk.Button(root, text="Speak", command=get_voice_input,bg="blue", fg="white", font=("Arial", 14))
voice_button.pack(pady=20)
voice_button.place(x=1150,y=495)

# Create a label for the options prompt
options_label = tk.Label(root, text="Select Options from below:", fg='black', font=("Arial", 12, "bold")) #bg='grey'
options_label.pack(pady=30)
options_label.place(x=150,y=495)

# Create a frame for the options buttons
options_frame = tk.Frame(root) #bg='grey'
options_frame.pack(pady=10)
options_frame.place(x=200,y=525)

# Create buttons for options
options_buttons = [tk.Button(options_frame, text="", bg='white', command=lambda: None,font=("Arial", 9)) for _ in range(10)]

# # Create buttons for options
# options_buttons = [tk.Button(root, text="", bg='light yellow', command=lambda: None) for _ in range(10)]  # Create 10 buttons for options

# Option mapping for user responses
option_mapping = {
    "new product": "1) New product",
    "customer support": "2) Customer support",
    "personal": "Personal",
    "home": "Home",
    "corporate": "Corporate",
    "back": "back",
    "Back": "Back",
    "close": "Close",
    "cancel":"cancel",
    "order now": "1) Order Now",
    "no more": "2) Know more",
    "pricing packages": "1) pricing packages",
    "availability": "2) availability",
    "delivery option": "3) delivery option",
    "troubleshooting an issue" : "1) Troubleshooting an issue",
    "warranty and repair": "2) Warranty and repair",
    "speak to an representative": "Speak to an representative",
    "connection issue": "1) Connection issue",
    "camera not working properly": "2) Camera not working properly",
    "mobile app issue": "3) Mobile app issue",
    "request a repair": "1) Request a repair",
    "request a replacement": "2) Request a replacement",
    "check your warranty status": "3) Check your warranty status",
    "basic package": " Basic package(2 camera, 1-year warranty)- ₹557",
    "advanced package": " Advanced package(4 camera, night vision, 2-year warranty)- ₹4,778",
    "premium package": " Premium package(6 camera, night vision, motion detection, 3-year warranty)- ₹12,557",
    "uttar Pradesh": "1) Uttar pradesh",
    "delhi": "2) Delhi",
    "madhya pradesh": "3) Madhya pradesh",
    "close": "Close",
    "same-day delivery": "3) Same-day delivery(₹55)",
    "express delivery": "2) Express delivery(1-2 buisness days, ₹25)",
    "standard delivery": "1) Standard delivery(3-5 business days, free)",
    "4) Not available in my location": "4) Not available in my location",
}
# Create the initial greeting and prompt for voice input
bot_response("Hello! Welcome to Securova Smart care! Please say 'Hello' to start.")
speak("Hello! Welcome to Securova Smart care! Please say 'Hello' to start.")
get_voice_input()  # Start the voice input process

# Run the Tkinter main loop
root.mainloop()
