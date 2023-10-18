from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import time
# from PIL import ImageTk , ImageOps , Image
# from playsound import playsound
def create_first_page():
    def goto_next_page():
        global first_name
        global last_name
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        if not first_name or not last_name:
            error_label.config(text="Please enter your name." , font=("Arial", 20))
        else:
            error_label.config(text="")
            window.destroy()

    window = tk.Tk()
    window.title("Game First Page")
    window.geometry("1353x652")
    window.configure(background="black")
    ABC= Frame(window, bg='black')
    ABC.grid(sticky='n' , padx= 10)
    ABC1= Frame(window, bg='pink' , width=350, height=900)
    ABC1.grid(row=0,column=0 , sticky='wn')
    ABC2=Frame(window,bg='black' , bd=20 , width=350,height=900)
    ABC2.grid( padx=1040,row=0 , column=0 ,columnspan=10 , sticky='ns')

    image_f = Image.open('//home//ayano//img//logo.jpg')
    image_f = image_f.resize((350, 250))
    photo_f = ImageTk.PhotoImage(image_f)
    label_f = tk.Label(ABC, image=photo_f, bg='black', justify=tk.CENTER)
    label_f.grid(sticky='w' , padx=435 , pady=10)
    
    image_l = Image.open('//home//ayano//img//lamp1.png')
    image_l = image_l.resize((350, 900))
    photo_l = ImageTk.PhotoImage(image_l)
    label_l = tk.Label(ABC2, image=photo_l, bg='black', justify=tk.CENTER)
    label_l.grid(sticky='e' , row=0 , column=0)
    
    image_r = Image.open('//home//ayano//img//lamp2.png')
    image_r = image_r.resize((350, 900))
    photo_r = ImageTk.PhotoImage(image_r)
    label_r = tk.Label(ABC1, image=photo_r, bg='black', justify=tk.CENTER)
    label_r.grid(sticky='w' , row=1 , column=0)
    
    first_name_label = ttk.Label(ABC, text="First Name :", foreground="white",  background="black", font=("Arial", 20))
    first_name_label.grid(pady=10  , sticky='w' , padx=540)
        
    first_name_entry = ttk.Entry(ABC, font=("Arial", 20))
    first_name_entry.grid(pady=2 ,  sticky='w' , padx=450)

    last_name_label = ttk.Label(ABC, text="Last Name :", foreground="white", background="black", font=("Arial", 20))
    last_name_label.grid(pady=10 , sticky='w' , padx=540)
    
    last_name_entry = ttk.Entry(ABC, font=("Arial", 20))
    last_name_entry.grid(pady=5 ,  sticky='w' , padx=450)
    
    next_button = tk.Button(ABC, text="Next", command=goto_next_page, font=("Arial", 20))
    next_button.grid(pady=25 ,  sticky='w' , padx=560)
   
    error_label = ttk.Label(ABC, foreground="red", background="black", font=("Arial", 12))
    error_label.grid()
    exit_buton = Button(window, text="⏎", font="Tahoma 14", bg="red", fg="black",width=2,height=1, bd=3, command=exit)
    exit_buton.grid(row=0, column=0, pady=2, sticky="nw" )
    window.mainloop()
create_first_page()
global first_name
global last_name
global mony1
mony1 =0
def create_last_page():
    window = tk.Tk()
    window.title("Game Next Page")
    window.geometry("1353x652")
    window.configure(background="black")
    ABC= Frame(window, bg='black' , width=800, height=700)
    ABC.grid(padx=250 , sticky='n')
    ABC1= Frame( bg='black' , width=500, height=100)
    ABC1.grid(row=0,column=0 , sticky='n' , pady=30)
    ABC2 = Frame( bg='#eeeeee' , width=400, height=50)
    ABC2.grid(row=0,column=0 , sticky='nw' , pady=306 , padx=500)
    ABC3 = Frame( bg='white' , width=350, height=50)
    ABC3.grid(row=0,column=0 , sticky='nw' , pady=389 , padx=600)
    ABC4 = Frame(bg='black' , width=500, height=500)
    ABC4.grid(row=0 , column=0 , padx=1, sticky='en' ,pady=200 )
    piroz = Label(ABC1 ,text=' " PÎROZ BE " ', font="Tahoma 25 bold" , bg='black' , fg='white'  )
    piroz.grid()
    image_f = Image.open('//home//ayano//img//shek.png')
    image_f = image_f.resize((800, 700))
    photo_f = ImageTk.PhotoImage(image_f)
    label_f = tk.Label(ABC, image=photo_f, bg='black' )
    label_f.grid()
    full_name_label = ttk.Label(ABC2, text=f"{first_name} {last_name}", foreground="black", background="#eeeeee", font=("Arial", 30))
    full_name_label.grid()
    mony = Label(ABC3,text=mony1,foreground="red", background="white", font=("Arial", 23 ))   
    mony.grid()
    restar = Button(ABC4,text= "Restart" ,font=('arial', 11, 'bold'),bg='#757575',fg="black",bd=5,width=18,height=2 , command= restart)
    restar.grid(row=1, column=0, padx=1)
    exit = Button(ABC4,text= "Exit" ,font=('arial 10', 11, 'bold'),bg='#757575',fg="black",bd=5,width=18,height=2  ,command=window.destroy)
    exit.grid(row=3,  column=0, padx=1 ,pady=30 , sticky='e')
    window.mainloop()
def update_mony(new_value):
    global mony1
    mony1 = new_value
    return mony1
root = Tk()
root.title("how winer is milion")
root.geometry("1353x652")
root.configure(bg="black")
ABC= Frame(root, bg='black')
ABC.grid(sticky='n')
ABC1= Frame(root, bg='black' , bd=20, width=1500, height=00)
ABC1.grid(row=0,column=0 , sticky='n')
ABC2=Frame(root,bg='black' , bd=20 , width=450,)
ABC2.grid( padx=1040,row=0 , column=0 ,columnspan=10 , sticky='ns')
ABC3=Frame(ABC1,bg='black' , bd=20 , width=900 , height=200)
ABC3.grid(row=0,column=0)
ABC4=Frame(ABC1,bg='black' , bd=20 , width=900 , height=150)
ABC4.grid(row=1,column=0)
ABC5=Frame(ABC1,bg='black' , bd=20 , width=900 , height=200)
ABC5.grid(row=2,column=0 ,sticky='ns' , padx=10)
ABC6=Frame(ABC1,bg='black' , bd=20 , width=900 , height=200)
ABC6.grid(row=2,column=0 , pady=87)
ABC7=Frame(root,bg='black', bd=5 , width=100 , height=60)
ABC7.grid(row=0 , column= 0 ,sticky='nsw', columnspan=8 , padx=530 , pady=405)
def hezif_x():
    # playsound('//home//ayano//deng//buten.mpga')
    image = Image.open("//home//ayano//img//x50_50.jpeg")
    image= image.resize((160,80))
    photo = ImageTk.PhotoImage(image) 
    label = Label(ABC3, image=photo , bg='black', bd=3 )
    label.grid(row=0,column=0 ,padx=10 )
    label.configure(image=photo)
    label.image = photo
    delet()
def x_gpt():
    # playsound('//home//ayano//deng//buten.mpga')
    image = Image.open("//home//ayano//img//xgpt.jpeg")
    image = image.resize((160, 80))
    photo = ImageTk.PhotoImage(image)
    label2 = Label(ABC3, image=photo, bg='black', bd=3 )
    label2.grid(row=0,column=2 , padx=10)
    label2.configure(image=photo)
    label2.image = photo
    global random_question
    obj = buten()
    if Ans1.get() == random_question['correct_answer']:
        obj.A.config(bg='green')
    if Ans2.get() == random_question['correct_answer']:
        obj.B.config(bg='green')
    if Ans3.get() == random_question['correct_answer']:
        obj.C.config(bg='green')
    if Ans4.get() == random_question['correct_answer']:
        obj.D.config(bg='green')  
def x_tebdil():
    # playsound('//home//ayano//deng//buten.mpga')
    image = Image.open("//home//ayano//img//xtebdil.jpeg")
    image = image.resize((160, 80))
    photo = ImageTk.PhotoImage(image)
    label1 = Label(ABC3, image=photo , bg='black', bd=3)
    label1.grid(row=0,column=1 ,padx=10 ,)
    label1.configure(image=photo)
    label1.image = photo
    update_question()
    time()
def delet():
    global random_question
    obj = buten()
    answer = []
    buteen = [obj.A , obj.B, obj.C, obj.D]
    for i in buteen:
        if i['text'] == random_question['correct_answer']:
            answer.append(i)
        else:
            buteen.remove(i)
            i.config(state='disabled')
            i.config(bg='black')
def pict1():
    image= Image.open("//home//ayano//img//Picture1.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('100')
def pict2():
    image= Image.open("//home//ayano//img//Picture2.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('200')
def pict3():
    image= Image.open("//home//ayano//img//Picture3.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('300')
def pict4():
    image= Image.open("//home//ayano//img//Picture4.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('500')
def pict5():
    image= Image.open("//home//ayano//img//Picture5.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('1,000')
def pict6():
    image= Image.open("//home//ayano//img//Picture6.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('2,000')
def pict7():
    image= Image.open("//home//ayano//img//Picture7.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('4,000')
def pict8():
    image= Image.open("//home//ayano//img//Picture8.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('8,000')
def pict9():
    image= Image.open("//home//ayano//img//Picture9.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('16,000')
def pict10():
    image= Image.open("//home//ayano//img//Picture10.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('32,000')
def pict11():
    image= Image.open("//home//ayano//img//Picture11.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('64,000')
def pict12():
    image= Image.open("//home//ayano//img//Picture12.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('125,000')
def pict13():
    image= Image.open("//home//ayano//img//Picture13.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('250,000')
def pict14():
    image= Image.open("//home//ayano//img//Picture14.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('500,000')
def pict15():
    image= Image.open("//home//ayano//img//Picture15.png")
    image = image.resize((300,600))
    photo = ImageTk.PhotoImage(image)
    label_m = Label(ABC2, image=photo , bg='black')
    label_m.grid(row=0 , column=1 , pady=70 )
    label_m.configure(image=photo)
    label_m.image = photo
    update_mony('1,000,000 milion')
    pack()
#توقيت 
timer_id = None
def time():
    def timee(seconds):
        global timer_id
        if timer_id is not None:
            root.after_cancel(timer_id)
        if seconds > 0:
            label_time.configure(text=f"Time {seconds}")
            timer_id = root.after(1000,timee, seconds - 1)
        else:
            pack()

    label_time= Label(ABC7, font="Tahoma 20 bold" ,bd=5 , bg='black' , fg='white')
    label_time.grid(row=0,  column=0 )
    timee(30)
pichk = ['pict1()' , 'pict2()' , 'pict3()' , 'pict4()' , 'pict5()' , 'pict6()' , 'pict7()' , 'pict8()' , 'pict9()' , 'pict10()', 'pict11()' , 'pict12()' , 'pict13()' , 'pict14()' , 'pict15()' ]
z = []
def pich():
    for i in range(1):
        eval(pichk[0])
        z.append(pichk.pop(0))  
questions =[
    {
        'question': "Bi qasî ku dîrokî bibî tu ewqasî dîkarî bi\n rastiye re be ev nirxandin kê kirye ?",
        'options': ["Rêber APO", "Aristo", "Mandella", "sokrat"],
        'correct_answer': "Rêber APO"
    },
    {
        'question': "Kovara yekemîn a kurdî ku bi tîpên latînî tê çapkirin kîjane ?",
        'options': ["RONAHî", "BOTSN", "HêVî", "HAWAR"],
        'correct_answer': "HAWAR"
    },
    {
        'question': "Nivîskarê destana MEM u ZîN kiye ?",
        'options': ["Ehmedê xanê", "feqiyê teyran", "mellayê cizîrî", "şakiro"],
        'correct_answer': "Ehmedê xanê"
    },
    {
        'question': "Girê miştenûr li kîjan bajarê kurdane ?",
        'options': ["Efrîn", "Kobanê", "Amûdê", "Dêrika hemko"],
        'correct_answer': "Kobanê"
    },
    {
        'question': "Hevpeymana Lozanê ya ku Kurdistanê di navbera \nSefewiya û osmaniya de parçe kir kengî bû ?",
        'options': ["1920", "1923", "1921", "1925"],
        'correct_answer': "1923"
    },

    {
        'question': "Gûndê bêrez konê bêpez mirozê ku bibêje.....ji\n çi re ne kîjan tê cihê vala..",
        'options': ["ez û ez", "ez û tû", "em û ez", "ew û ez"],
        'correct_answer': "ez û ez"
    },
    {
        'question': "Klan ji çend kesan pêk tê ?",
        'options': ["20-25", "30-35", "40-45", "50-55"],
        'correct_answer': "30-35"
    },
    {
        'question': "Hîlala zêrîn li kur dîkeve ?",
        'options': ["seudî erebîstan", "îraq", "îran", "Toros zagros"],
        'correct_answer': "Toros zagros"
    },
    {
        'question': "Kîjan ji van di serdema neolotîk de hatiye\n îcad kirin û pêşxistin ?",
        'options': ["çanda jin-xwedawend", "çanda baviksalarî-şamantî", "çanda desthiltdarî", "çanda hiyarereşîk-tebeqat"],
        'correct_answer': "çanda jin-xwedawend"
    },
    {
        'question': "Komkujiya Helebçe ya ku bi destê Seddam Huseeyin bi çekên \nkîmyawî li ser gelê kurd hate kirin kengî bû ?",
        'options': ["16 Adarê 1980", "21 Adarê 1979", "1 Gulan 1984", "19 Cotmehê 1974"],
        'correct_answer': "16 Adarê 1980"
    },
    {
        'question': "Partiya karekerê kurdistanê (PKK) kengî hatiye \ndamezrandin ?",
        'options': ["27 mijdarê 1979", "28 mijdarê 1978", "27 mijdarê 1978", "27 mijdarê 1977"],
        'correct_answer': "27 mijdarê 1979"
    },
    {
        'question': "Dîroka ji nûve dayikbuna gelê kurd \njidayikbûna RêBER APO kengiye ?",
        'options': ["4ê nîsan 1945", "4ê nîsan 1946", "4ê nîsan 1947", "4ê nîsan 1948"],
        'correct_answer': "4ê nîsan 1945"
    },
    {
        'question': "Navê beşa zanistî ya ku rewêa hewatê dişopîne çiye ?",
        'correct_answer': "etîmolojî",
        'options': ["epîstomolojî", "meteolojî", "etîmolojî", "krîptolojî"]
        
    },
    {
        'question': "girara zivistanê......dikele kîjan tê cihê vala",
        'correct_answer': "havînê",
        'options': ["havîn", "payiz", "bihar", "her tim"]
  
    },
    {
        'question': " mamê ji deştê tê û barek strî l piştê ye ?",
        'correct_answer': "jujî",
        'options': ["kusî", "req", "xezal", "jujî"]
  
    },
    {
        'question': "çiyayê herî bilind di dunyayê de kîjane?",
        'correct_answer': "êvêrêst",
        'options': ["hîmalaya", "zagros", "kezwana", "êvêrêst"]
  
    },
    {
        'question': "sembola kîmyawî ya zêr çiye?",
        'correct_answer': "Au",
        'options': ["Zn", "Z", "Au", "H2o"]
  
    },
    {
        'question': "kê wêneya mona lisa xêz kiriye?",
        'correct_answer': "da vînşî",
        'options': ["pîkaso", "Da vînşî", "loy kiyalî", "kail john"]
  
    },
    {
        'question': " paytexa fransa kijane?",
        'correct_answer': "parîs",
        'options': ["kolne", "keteloniya", "parîs", "roma"]
  
    },
    {
        'question': "Li kîjan saetê heta 60 deqîqeyan hefteya\n li dijî bêxwedî tiştan hatîye damezrandin?",
        'correct_answer': "Saet 22:00",
        'options': ["Saet 20:00", "Saet 21:00", "Saet 22:00", "Saet 23:00"]
    },
    {
        'question': "Kîjan jîngehê pirsa 'Koçber' tê dîtin?",
        'correct_answer': "Ji Kurdistana Başûr ber bi Tirkiyê ve",
        'options': ["Ji Kurdistana Başûr ber bi Îranê ve", "Ji Kurdistana Başûr ber bi Tirkiyê ve\n", "Ji Kurdistana Başûr ber bi Sûriyê ve", "Ji Kurdistana Başûr ber bi Iraqê ve"]
    },
    {
        'question': "Li kîjan kantona Tirkiyê bajarê Amedê (Diyarbakir) ye?",
        'correct_answer': "Kantona Îçel",
        'options': ["Kantona Mêrdîn", "Kantona Vanê", "Kantona Bingolê", "Kantona Îçel"]
    },
    {
        'question': "Kîjan rojhilata Amerîka ji rojhilata bavê derxistî ye?",
        'correct_answer': "Rojhilata Navîn",
        'options': ["Rojhilata Navîn", "Rojhilata Bakur", "Rojhilata Başûr", "Rojhilata Rojava"]
    },
    {
        'question': "Kîjan pirtûka Elî Ferhat û Şêxê Elih \ndi sala 1936'an de hatiye weşandin?",
        'correct_answer': "Mem û Zîn",
        'options': ["Lîs û Memê Alan", "Mem û Zîn", "Dil û Ferheng", "Gulê Sara û Zozan"]
    },
    {
        'question': "Li kîjan bajarê Îngilîstanê Big Ben tê dîtin?",
        'correct_answer': "London",
        'options': ["Manchester", "Liverpool", "Birmingham", "London"]
    },
    {
        'question': "Li kîjan welatê Asyayê jiyana 'Gautama Buddha' dest pê kir?",
        'correct_answer': "Endonezya",
        'options': ["Taywan", "Çîn", "Hindistan", "Endonezya"]
    },
    {
        'question': "Kîjan bajaran bi navê 'şemiyekîyan' tên nasîn?",
        'correct_answer': "Hewlêr, Soran û Koye",
        'options': ["Hewlêr, Dihok û Silêmanî", "Hewlêr, Soran û Koye\n", "Soran, Koye û Silêmanî", "Silêmanî, Dihok û Koye"]
    },
    {
        'question': "Li kîjan salê Amerîka wekî dewlet hatîye damezrandin?",
        'correct_answer': "1776",
        'options': ["1642", "1776", "1812", "1865"]
    },
    {
        'question': "Çima dinya bi teyrên ser şikestî ye?",
        'correct_answer': "Ji ber ku ji lêlekê çend kilometre dûr in",
        'options': ["Ji ber ku lêlekên wan pir şaş in", "Ji ber ku ji lêlekê çend kilometre dûr in\n", "Ji ber ku wan ji hêla erdnîgariyê hatine amade kirin", "Ji ber ku çima ne ji bilî wê dikarin lê bibin"]
    },
    {
        'question': "Li kîjan kargehê mirov dikare matematîkê bikar bîne?",
        'correct_answer': "Zanistxane",
        'options': ["Bûroya xizmetê", "Serbixwekarî", "Zanistxane", "Bazirganî"]
    },
    {
        'question': " Xwendina hijmara 2000022 a rast kîjane?",
        'correct_answer': "Du milyon û bîst û dudu",
        'options': ["dused hezar û bîst û dudu", "bîst hezar û bîst û dudu\n", "du hezar û bîst û dudu", "Du milyon û bîst û dudu"]
    },
    {
        'question': "kîjan ji van bajaran ne cîranin ?",
        'correct_answer': "Amûdê-tirbesipî",
        'options': ["Dêrik-çilaxa", "Kobanê-Riha", "Qamişlo-Amûdê", "Amûdê-tirbesipî"]
    },
    {
        'question': " kîjan ji bo kesê ku xwe li ser pişta \nhinekadin xwe xwedî dikin tê gotin?",
        'correct_answer': "Kurtêlxur",
        'options': ["Kurtêlxur", "xemxur", "çavsor", "xwînxwar"]
    },
    {
        'question': " Di hevoka (Ezê biçim çiya) de kîjan hêman tune ye?",
        'correct_answer': "bireser",
        'options': ["pêvber", "kirde", "têrker", "bireser"]
    },
    {
        'question': " Di laşê mirov de cihê ku hestî dighêje hev ?",
        'correct_answer': "Movik",
        'options': ["Serik", "Movik", "kovik", "Tovik"]
    },
    {
        'question': " kîjan ji dervaî xwe xwîn nikare bigre?",
        'correct_answer': "O",
        'options': ["B", "A", "O", "AB"]
    },
    {
        'question': "braziyê sayid riza yê ku di berxwedana dêrsimê de dibe\n îxantkar navê wî çiye ?",
        'correct_answer': "Rêber",
        'options': ["hiso", "şemo", "Rêber", "xidir"]   
    },
    {
        'question': " li ruyê erdê çend okyanus hene ?",
        'correct_answer': "7",
        'options': ["9", "7", "5", "4"]  
    },
    {
        'question': "kîjan nivîskarê kurd bi navê herekolê ezîzan tê naskirin  ?",
        'correct_answer': "celadet elî bedirxan",
        'options': ["celadet elî bedirxan", "erebê şemo", "elîyê ebdilrehman", "heciyê cudî"]
    },
    
    {
        'question': "di sala 2011 de li li rojavayê kurdîstanê şoreş\n destpêkir di kîjan mehê de bû ?",
        'correct_answer': "19 tîrmeh",
        'options': ["19 adar", "19 gulan", "19 tebax", "19 tîrmeh"] 
    },
    {
        'question': "15ê Tebaxê ku fîşeka yekê ji bo azadiya gelê kurd hat\n teqandin bi pêşengiya kê bû ?",
        'correct_answer': "ş.Egîd(Mahsum korkmaz)",
        'options': ["ş.Egîd(Mahsum korkmaz)", "ş.Heqî qarer", "ş.Mazlûm dogan", "ş.Memed hayrî durmuş"]
    },
    {
        'question': " Felsefa zerdeşt kîjan ji van xalan di nav xwe de dihewîne ?",
        'correct_answer': "derwêşane jiyankirin",
        'options': ["jiyan bike ji bo navê xwe bixî dîrokê", "gerdun di nava xwede jiyan kirin\n", "Derwêşane jiyan", "her tiştî bike tu carek jiyan dikî"]   
    },
    {
        'question': "kîjan ji van ne rêbazek ya destgirtina dîrokê ye ?",
        'correct_answer': "kesên nav û deng naskirin",
        'options': ["kronolojîk", "kesên nav û deng naskirin", "çîrokî", "disthiladar"]   
    },
    {
        'question': " Di zaraveykî kurdî de kîjan dibe Dîrok?",
        'correct_answer': "mêjû",
        'options': ["mêju", "tarîx", "mêjî", "demo"]   
    },
    {
        'question': "çanda tilxelef ka dîrokî li kuderê ye ?",
        'correct_answer': "Serêkaiye",
        'options': ["Wan", "sinê", "Serêkaiyê", "Skilêmanî"]   
    },
    {
        'question': "şikefta şanîdar ya ku yekemîn car hestuyên însan lê hat \ndîtîn li kuderê ye  ?",
        'correct_answer': "silêmanî",
        'options': ["silêmanî", "Kirmanêan", "Amed", "Hewlêr"]
    }
]
class buten:
    def __init__(self):
        global random_question
        self.A = buten_A = Button(ABC6,font=('arial', 14, 'bold'),bg='blue',fg="white",bd=5,width=25,height=2,textvariable=Ans1,
        command=lambda:(x(Ans1.get()) , buten_A.config(bg='red') if Ans1.get() != random_question['correct_answer'] else None ), justify=CENTER, )
        buten_A.grid(row=1, column=1, pady=4, padx=20)
        self.B = buten_B = Button(ABC6,font=('arial', 14, 'bold'),bg='blue',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans2
        ,command=lambda: (x(Ans2.get()) ,  buten_B.config(bg='red') if Ans2.get != random_question['correct_answer']   else  None ))
        buten_B.grid(row=1, column=3, pady=4, padx=10)
        self.C = buten_C = Button(ABC6,font=('arial', 14, 'bold'),bg='blue',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans3,
        command=lambda: (x(Ans3.get()) , buten_C.config(bg='red') if Ans3.get != random_question['correct_answer'] else None))
        buten_C.grid(row=2, column=1, pady=4, padx=10)
        self.D = buten_D = Button(ABC6,font=('arial', 14, 'bold'),bg='blue',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans4,
        command=lambda: (x(Ans4.get()) , buten_D.config(bg='red') if Ans4.get != random_question['correct_answer'] else None))
        buten_D.grid(row=2, column=3, pady=4, padx=10) 
def update_question():
    global random_question
    random_question = random.choice(questions) 
    Qes1.set(random_question['question'])
    Ans1.set(random_question['options'][0])
    Ans2.set(random_question['options'][1])
    Ans3.set(random_question['options'][2])
    Ans4.set(random_question['options'][3])
    questions.remove(random_question)
    buten()
def x(answer):
    global random_question
    if answer == random_question['correct_answer']:
        update_question()
        time()
        pich()
    else:
        x=Label(ABC7,text='Game over',font="Tahoma 20 bold" ,bd=5 , bg='black' , fg='red')
        x.grid(row=0,  column=0 )
        if Ans1.get() == random_question['correct_answer']:
            buten_a = Button(ABC6,font=('arial', 14, 'bold'),bg='green',fg="white",bd=5,width=25,height=2,textvariable=Ans1,justify=CENTER, )
            buten_a.grid(row=1, column=1, pady=4, padx=20)
        elif Ans2.get() == random_question['correct_answer']:
            buten_b = Button(ABC6,font=('arial', 14, 'bold'),bg='green',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans2)
            buten_b.grid(row=1, column=3, pady=4, padx=10)
        elif Ans3.get() == random_question['correct_answer']:
             buten_c = Button(ABC6,font=('arial', 14, 'bold'),bg='green',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans3,)
             buten_c.grid(row=2, column=1, pady=4, padx=10)
        elif Ans4.get() == random_question['correct_answer']:
            buten_d = Button(ABC6,font=('arial', 14, 'bold'),bg='green',fg="white",bd=5,width=25,height=2,justify=CENTER,textvariable=Ans4,)
            buten_d.grid(row=2, column=3, pady=4, padx=10)    
        root.after(1000, pack)
def pack():
    root.destroy()
    create_last_page()
Qes1 = StringVar()
Ans1 = StringVar()
Ans2 = StringVar()
Ans3 = StringVar()
Ans4 = StringVar()
update_question()
time()
image = Image.open("//home//ayano//img//hezif.jpeg")
image = image.resize((160,80))
photo = ImageTk.PhotoImage(image)
label = Button(ABC3, image=photo , bg='black', bd=3 , command=hezif_x)
label.grid(row=0,column=0 , padx=10)  

image2 = Image.open("//home//ayano//img//gpt.jpeg")
image2 = image2.resize((160,80))
photo2 = ImageTk.PhotoImage(image2)
label2 = Button(ABC3, image=photo2 , bg='black', bd=3 ,command=x_gpt )
label2.grid(row=0,column=2 , padx=10)

image1 = Image.open("//home//ayano//img//tebdil.jpg")
image1 = image1.resize((160,80))
photo1 = ImageTk.PhotoImage(image1)
label1 = Button(ABC3, image=photo1 , bg='black', bd=3, command=x_tebdil)
label1.grid(row=0,column=1 ,padx=10 ,)

image_f = Image.open('//home//ayano//img//logo.jpg')
image_f = image_f.resize((350,250))
photo_f = ImageTk.PhotoImage(image_f)
label_f = Label(ABC4, image=photo_f , bg='black' , justify=CENTER)
label_f.grid(row=0 , column=0 , pady=5)

image_m = Image.open("//home//ayano//img//Picture0.png")
image_m = image_m.resize((300,600))
photo_m = ImageTk.PhotoImage(image_m)
label_m = Label(ABC2, image=photo_m , bg='black')
label_m.grid(row=0 , column=1  , pady=70 )

#ازرار

enter = Label(ABC5, font="Tahoma 15 bold" , bg='blue' , fg='white' , width=60 ,bd=5 , justify=CENTER ,relief='raised' , textvariable=Qes1 )
enter.grid(row=0 , column=1 , padx=150 ,columnspan=6 , sticky="n" )

labl_A= Label (ABC6, font=('arial',14,'bold'),text="A:",bg='black' ,fg='white',bd=5)
labl_A.grid(row=1 , column=0, pady=4,)

labl_B= Label (ABC6, font=('arial',14,'bold'),text="B:",bg='black', fg='white',bd=5,justify=LEFT)
labl_B.grid(row=1 , column=2)

labl_C= Label (ABC6, font=('arial',14,'bold'),text="C:",bg='black' ,fg='white',bd=5, justify=LEFT )
labl_C.grid(row=2 , column=0)

labl_D= Label (ABC6, font=('arial',14,'bold'),text="D:",bg='black' ,fg='white',bd=5, justify=LEFT )
labl_D.grid(row=2 , column=2)

exit_button = Button(root, text="⏎", font="Tahoma 14", bg="red", fg="black",width=2,height=1, bd=3, command=exit)
exit_button.grid(row=0, column=0, pady=2, sticky="nw" )



root.mainloop()