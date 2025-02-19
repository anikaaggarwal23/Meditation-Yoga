import csv
def lino():
    print("*"*80)
def med():
    import csv
    with open('meditation.csv','w') as file:
        writer = csv.writer(file)
        lak=["SNO.","DATA","PERCENTAGE"]
        writer.writerow(lak)
        a=[1,"Americans who have meditated at least once:-",14]
        b=[2,"US children who regularly practice meditation.:-",7]
        c=[3,"Americans claim to meditate at least once a week.:-",40]
        d=[4,"popularity of meditation by age group:45-64 age group:-",15.9]
        e=[5,"popularity of meditation by age group:18-44 age group:-",13.4]
        f=[6,"popularity of meditation by age group:65+ age group:-",13.4]
        g=[7,"percentage of women meditating:-",10.3]
        h=[8,"percentage of men meditating:-",5.2]
        i=[9,"Meditation can reduce your chance of being hospitalized for coronary heart disease by :-",87]
        j=[10,"Meditation can increase employees’ productivity by:-",120]
        k=[11,"Meditation can reduce the wake time of people with insomnia by:-",50]
        l=[12,"Mindfulness meditation can reduce symptoms of post-traumatic stress disorder ",73]
        m=[13,"Meditation improves anxiety levels :-",60]
        n=[14,"Meditation can reduce PMS symptoms:-",57]
        o=[15,"Due to meditation School suspensions were reduced by :-",45]
        z=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
        writer.writerows(z)
    with open("meditation.csv",'r') as file:
        csv_file = csv.reader(file)
        next(csv_file,None)
        for row in csv_file:
            if row==[]:
                continue
            else:
                q=row[0]
                r=row[1]
                s=row[2]
                print(q,r,s,"%")
def yoga1():
    import csv
    with open('yoga.csv','w') as file:
        writer = csv.writer(file)
        lak=["SNO.","DATA","PERCENTAGE"]
        writer.writerow(lak)
        a=[1,"current US population practicing yoga :-",10]
        b=[2,"Percentage of male yoga practitioners:-",28]
        c=[3,"Percentage of yoga practitioners who practice yoga 2–3 times a week.:-",44]
        d=[4,"Percentage of yoga practitioners are 18 – 29 year olds:-",19]
        e=[5,"Percentage of yoga practitioners are 30 – 49 year olds:-",43]
        f=[6,"Percentage of yoga practitioners are 50+ year old:-",38]
        g=[7,"percentage of women practicing yoga:-",72]
        h=[8," US yogis do yoga because it helps them release tension:-",54]
        i=[9," US yogis eat healthily because of yoga :-",40]
        j=[10,"US yoga practitioners believe that yoga helps them sleep better.:-",59]
        k=[11,"Percentage of yogis who want to try laughter yoga:-",20]
        l=[12," In Japan, the growth rate of yoga",413]
        m=[13,"Percentage of people start to improve flexibility:-",61]
        n=[14,"Percentage of start to improve physical fitness:-",44]
        o=[15,"Percentage of people start for overall health :-",49]
        z=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
        writer.writerows(z)
    with open("yoga.csv",'r') as file:
        csv_file = csv.reader(file)
        next(csv_file,None)
        for row in csv_file:
            if row==[]:
                continue
            else:
                q=row[0]
                r=row[1]
                s=row[2]
                print(q,r,s,"%")

def health():
    import csv
    print("**********************MENTAL HEALTH STATISTICS******************************")
    print("1.MENTAL ILLNESS\n2.MENTAL HEALTH CARE MATTERS\n3.DEPRESSION\n4.SUICIDE RATE\n5.EXIT")
    while True:
        ch=int(input("ENTER  YOUR CHOICE:-"))
        if ch==1:
            print("::::::::::::::::::::MENTAL ILLNESS STATISTICS:::::::::::::::::::::::::::")
            with open('illness.csv','w') as file:
                writer = csv.writer(file)
                lak=["SNO.","DATA","PERCENTAGE"]
                writer.writerow(lak)
                a=[1," U.S. adults experienced mental illness in 2020 (52.9 million people).  :-",22]
                b=[2,"U.S. adults experienced serious mental illness in 2020 (14.2 million people):-",5.6]
                c=[3,"U.S. youth aged 6-17 experienced a mental health disorder in 2016 (7.7 million people):-",16.5]
                d=[4," U.S. adults experienced a co-occurring substance use disorder and mental illness in 2020 (17 million people):-",6.7]
                e=[5,"Annual prevalence among U.S. adults, by condition Major Depressive Episode:-", 8.4]
                f=[6,"Annual prevalence among U.S. adults, by condition Schizophrenia:-",1]
                g=[7,"Annual prevalence among U.S. adults, by condition Bipolar Disorder:-",2.8]
                h=[8," Annual prevalence among U.S. adults, by condition Anxiety Disorders:-",19.1]
                i=[9," Annual prevalence among U.S. adults, by condition Posttraumatic Stress Disorder:-",3.6]
                j=[10,"Annual prevalence among U.S. adults, by condition Obsessive Compulsive Disorder:-",1.2]
                z=[a,b,c,d,e,f,g,h,i,j]
                writer.writerows(z)
            with open("illness.csv",'r') as file:
                csv_file = csv.reader(file)
                next(csv_file,None)
                for row in csv_file:
                    if row==[]:
                        continue
                    else:
                        q=row[0]
                        r=row[1]
                        s=row[2]
                        print(q,r,s,"%")
        elif ch==2:
            print("::::::::::::::::::::MENTAL HEALTH CARE STATISTICS:::::::::::::::::::::::::::")
            with open('care.csv','w') as file:
                writer = csv.writer(file)
                lak=["SNO.","DATA","PERCENTAGE"]
                writer.writerow(lak)
                a=[1," U.S. adults with mental illness received treatment in 2020:-",46.2]
                b=[2,"U.S. adults with serious mental illness received treatment in 2020:-",64.5]
                c=[3," U.S. youth aged 6-17 with a mental health disorder received treatment in 2016  :-",50.6]
                d=[4," U.S. adults with mental illness had no insurance coverage in 2020:-",11]
                e=[5,"U.S. adults with serious mental illness had no insurance coverage in 2020:-",11.3]
                f=[6,"Annual treatment rates among U.S. adults with any mental illness, by demographic group MALE:-",37.4]
                g=[7,"Annual treatment rates among U.S. adults with any mental illness, by demographic groupFEMALE:-",51.2]
                h=[8,"Annual treatment rates among U.S. adults with any mental illness, by demographic group GAY:-",54.3]
                i=[9,"Annual treatment rates among U.S. adults with any mental illness, by demographic group LATINO:-",35.1]
                j=[10,"Annual treatment rates among U.S. adults with any mental illness, by demographic group Non-Hispanic Asian:-",20.8]
                z=[a,b,c,d,e,f,g,h,i,j]
                writer.writerows(z)
            with open("care.csv",'r') as file:
                csv_file = csv.reader(file)
                next(csv_file,None)
                for row in csv_file:
                    if row==[]:
                        continue
                    else:
                        q=row[0]
                        r=row[1]
                        s=row[2]
                        print(q,r,s,"%")
        elif ch==3:
            print("::::::::::::::::::::SUICIDE RATE STATISTICS:::::::::::::::::::::::::::")
            with open('suicide.csv','w') as file:
                writer = csv.writer(file)
                lak=["SNO.","DATA","PERCENTAGE"]
                writer.writerow(lak)
                a=[1,"people who die by suicide had a diagnosed mental health condition:-",46]
                b=[2,"people who die by suicide may have experienced symptoms of a mental health condition, according to interviews with family, friends and medical professionals (also known as psychological autopsy):-",90]
                c=[3," Annual prevalence of serious thoughts of suicide, by U.S. demographic group adults :-",4.9]
                d=[4,"Annual prevalence of serious thoughts of suicide, by U.S. demographic group  young adults aged 18-25:-",11.3]
                e=[5,"Annual prevalence of serious thoughts of suicide, by U.S. demographic group  high school students:-",18.8]
                f=[6,"Annual prevalence of serious thoughts of suicide, by U.S. demographic group LGBTQ youth:-",45]
                g=[7," people who die by suicide are male:-",79]
                h=[8,"deaths in South Korea in 2019 were from suicide:-",4.5]
                i=[9,"deaths in Quatar were from suicide:-",3]
                j=[10,"deaths in Sri Lanka were from suicide:-",3.3]
                z=[a,b,c,d,e,f,g,h,i,j]
                writer.writerows(z)
            with open("suicide.csv",'r') as file:
                csv_file = csv.reader(file)
                next(csv_file,None)
                for row in csv_file:
                    if row==[]:
                        continue
                    else:
                        q=row[0]
                        r=row[1]
                        s=row[2]
                        print(q,r,s,"%")
        elif ch==4:
            print("::::::::::::::::::::DEPRESSION STATISTICS:::::::::::::::::::::::::::")
            with open('depression.csv','w') as file:
                writer = csv.writer(file)
                lak=["SNO.","DATA","PERCENTAGE"]
                writer.writerow(lak)
                a=[1,"U.S. population age 18 and older who suffer from DEPRESSION:-",7.1]
                b=[2,"cancer patients experience depression:-",25]
                c=[3," post-stroke patients experience depression-",27]
                d=[4,"Parkinson’s disease patients may experience depression:-",50]
                e=[5,"anorexia patients have a comorbid mood disorder, such as depression.:-",49]
                f=[6,"women living with polycystic ovary syndrome experience depression:-",20]
                g=[7,"unsuccessful treatment for depression is due to medical non-compliance:-",50]
                h=[8,"people in low- and middle-income countries receive no treatment :-",75]
                i=[9,"Participation in a DBSA patient-to-patient support group improved treatment compliance by almost :-",86]
                j=[10,"Support group participants willing to take medication and cope with side effects.:-",84]
                z=[a,b,c,d,e,f,g,h,i,j]
                writer.writerows(z)
            with open("depression.csv",'r') as file:
                csv_file = csv.reader(file)
                next(csv_file,None)
                for row in csv_file:
                    if row==[]:
                        continue
                    else:
                        q=row[0]
                        r=row[1]
                        s=row[2]
                        print(q,r,s,"%")
        elif ch==5:
            print("****************EXITING************************")
            break
        else:
            print("::::WRONG CHOICE::::")           
def browserlink(a):
    import webbrowser
    webbrowser.open(a)
def linkspro():
    print("*****************:::::::LINKS::::::::::::::::*****************")
    print("1.WHAT IS MEDITATION?\n2.HOW TO MEDITATE\n3.EIGHT TYPES OF MEDITATION\n4.Meditation: A Scientific Guide on How to Meditate for Stress Reduction\n5.WHAT IS YOGA?\n6.HISTORY AND TYPES OF YOGA\n7.BENEFITS OF YOGA\n8.MENTAL HEALTH AND WELLBEING\n9.CARING FOR YOUR MENTAL HEALTH\n10.IMPORTANCE OF MENTAL HEALTH\n11.EXIT")
    while True:
        ch=int(input("enter the choice:"))
        if ch==1:
            browserlink("https://www.verywellmind.com/what-is-meditation-2795927")
        elif ch==2:
            browserlink("https://www.mindful.org/how-to-meditate/")
        elif ch==3:
            browserlink("https://www.medicalnewstoday.com/articles/320392")
        elif ch==4:
            browserlink("https://www.everydayhealth.com/meditation/")
        elif ch==5:
            browserlink("https://www.medicalnewstoday.com/articles/286745")
        elif ch==6:
            browserlink("https://www.dabur.com/amp/in/en-us/about/science-of-ayurveda/yoga/what-is-yoga-and-types-of-yoga")
        elif ch==7:
            browserlink("https://www.hopkinsmedicine.org/health/wellness-and-prevention/9-benefits-of-yoga")
        elif ch==8:
            browserlink("https://www.cdc.gov/mentalhealth/learn/index.htm#:~:text=Mental%20health%20includes%20our%20emotional,childhood%20and%20adolescence%20through%20adulthood.")
        elif ch==9:
            browserlink("https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health")
        elif ch==10:
            browserlink("https://vikaspedia.in/health/mental-health/importance-of-mental-health")
        elif ch==11:
            print("::::::::::::EXITING::::::::::::")
            break
        else:
            print(":::WRONG CHOICE:::")
def csvpro():
    print("**STATISTICS**")
    print("1.MEDITATION\n2.YOGA\n3.MENTAL HEALTH\n4.EXIT")
    while True:
        choice=int(input("enter the choice:-"))
        if choice ==1:
            print("::::::::::::MEDITATION STATISTICS:::::")
            med()
        elif choice==2:
            print("::::::::YOGA STATISTICS::::")
            yoga1()
        elif choice==3:
            print("::::::MENTAL HEALTH STATISTICS::::")
            health()
        elif choice==4:
            print("************EXITING****************")
            break
        else:
            print("WRONG CHOICE")


#***************************************TEXT FILE*****************************************************#
a= ":::::FACTS ON MEDITATION::::\n"
b="\t1. Meditation is a huge and growing trend and, unlike the practice itself, it shows no signs of slowing down.\n"
c="\t2. Meditation was born in India.Since 2012 the number of children meditating has increased more than 80%..\n"
d="\t3. Meditation as a practice is thought to be around 2,600 years old.\n"
e="\t4. Jainism, Taoism, and Confucianism propelled meditation techniques.\n"
f="\t5. Meditation is a tool which bring a balance in your life.It stops the mind chatter and unnecessary agitation thus bringing sense of Happiness, Satisfaction, compassion and love. If done properly and under proper guidance Mediation can permanently eliminates Anxiety, Stress, Fear and Sadness from life.\n"
g="\t6. It is one way bring calm which help in bring the coordination among Mind, body and soul.\n"
h="\t7. Meditation exercise experienced fewer negative thoughts in response to viewing negative images, compared with those in a control group .\n"
i="\t8. Some forms of meditation may help you develop a stronger understanding of yourself, helping you grow into your best self.\n"
j="\t9. Metta, a type of meditation also known as loving-kindness meditation, begins with developing kind thoughts and feelings toward yourself.\n"
k="\t10. Your perception of pain is connected to your state of mind, and it can be elevated in stressful conditions.So,meditation can help relax your mind as well as the pain.\n"
a1= "::::::FACTS ON YOGA::::::\n"
l='\t1. The word yoga comes from the Sanskrit language and means “union.”\n'
m="\t2. There are more than 100 styles of yoga. These include Vinyassa, Yin, Power, Hot, Iyengar, Ashtanga, Kundalini, and Kriya to name a few.\n"
n="\t3. Yoga boosts your immune system and eases depression.\n"
o="\t4. Yoga helps control Diabetes.\n"
p1="\t5. Yoga is over 5,000 years old and one of the oldest disciplines in the world.\n"
q1="\t6. Yoga was introduced to America in the 18th century.\n"
r1="\t7. Yoga is the most commonly used complementary health approach in the U.S.\n"
s="\t8. One in three Americans has tried yoga at least once. Survey results are taken from Yoga Alliance and Yoga Journal study.\n"
t="\t9. Flexibility and stress relief are some of the most popular reasons people start a yoga practice.\n"
u="\t10. Yoga in the workplace can help improve productivity.\n"
a2= ":::::::FACTS ON MENTAL HEALTH::::::\n"
v="\t1. The global economy loses about US$ 1 trillion per year in productivity due to depression and anxiety.\n"
w="\t2. Mental, neurological and substance use disorders make up 10% of the global burden of disease and 25.1% of non-fatal disease burden.\n"
x1="\t3. Around 1 in 7 of the world's adolescents have a mental disorder.\n"
y1="\t4. Depression is a common mental disorder. Globally, it is estimated that 5% of adults suffer from depression.\n"
z1="\t5. Globally, mental disorders account for 1 in 6 years lived with disability.\n"
ab="\t6. More than 700,000 people die by suicide every year. Suicide accounts for 1 in 100 deaths globally. Suicide is the fourth leading cause of death in individuals aged 15-29 years.\n"
bc="\t7. Around 1 in 9 people in settings affected by conflict have a moderate or severe mental disorder.\n"
cd="\t8. People with severe mental disorders die 10 to 20 years earlier than the general population.\n"
de="\t9. In low-income countries there are fewer than one mental health staff per 100,000 population, compared with more than 60 in high-income countries.\n"
ef="\t10. 40% of low-income countries do not include essential medicines that have been on the WHO Model list for essential medicines for decades, such as lithium carbonate mood stabilizer for bipolar disorder.\n"
a3="::::::::SIGNIFICANCE OF NUMBER 108::::::\n"
fg="\t1. Sanskrit alphabet has 54 letters. Each letter has a masculine (Shiva) and feminine (Shakti) energy 54 X 2 = 108.\n"
gh="\t2. Desires. There are said to be 108 earthly desires in mortals.\n"
hi="\t3. Time. It is said we have 108 feelings. 36 related to the past, 36 related to the present, and 36 related to the future.\n"
ij="\t4. Astrology. There are 12 constellations and 9 arc segments. There are 12 houses and 9 planets. 12 X 9 = 108.\n"
jk="\t5. The diameter of the sun is 108 times the earth.\n"
kl="\t6. The number is considered to be so auspicious that 108 is the number for emergency services in India.\n"
a4=":::::::SIGNIFICANCE OF MEDITATION IN NATURE:::::\n"
lm="\t1. Decreases Depression And Anxiety.\n"
mn="\t2. It Enhances Grey Matter Concentration In The Brain.\n"
no="\t3. Improves The Ability To Fight With Pain.\n"
op="\t4. Lowers Stress Levels And Panic.\n"
qr="\t5. Alerts Your Body And Mindfulness.\n"
rs="\t6. Improves Mood And Helps To Focus Better.\n"
st="\t7. Decreases The Risk Of Heart Ailments.\n"
tu="\t8. Lowered High Blood Pressure.\n"
a5=":::::::::::::::::7 CHAKRAS OF HUMAN BODY:::::::\n"
uv="\t1. The Root Chakra: Muladhara\n"
vw="\t2. The Sacral Chakra: Svadhisthana\n"
wx="\t3. The Solar Plexus Chakra: Manipura\n"
xy1="\t4. The Heart Chakra: Anahata\n"
yz="\t5. The Throat Chakra: Vishuddha\n"
za="\t6. The Third Eye Chakra: Ajna\n"
b1="\t7. The Crown Chakra: Sahasrara\n"
def meditation():
     f1=open("meditation.txt","w")
     f1.write(a)
     f1.write(b)
     f1.write(c)
     f1.write(d)
     f1.write(e)
     f1.write(f)
     f1.write(g)
     f1.write(h)
     f1.write(i)
     f1.write(j)
     f1.write(k)
     f1.close()
def meditation_display():
     f1=open("meditation.txt","r")
     s1=f1.readline()
     while s1:
          print(s1)
          s1=f1.readline()
     f1.close()
def yoga():
     f2=open("yoga.txt","w")
     f2.write(a1)
     f2.write(l)
     f2.write(m)
     f2.write(n)
     f2.write(o)
     f2.write(p1)
     f2.write(q1)
     f2.write(r1)
     f2.write(s)
     f2.write(t)
     f2.write(u)
     f2.close()     
def yoga_display():
     f2=open("yoga.txt","r")
     s2=f2.readline()
     while s2:
          print(s2)
          s2=f2.readline()
     f2.close()
def mental_health():
     f3=open("mental health.txt","w")
     f3.write(a2)
     f3.write(v)
     f3.write(w)
     f3.write(x1)
     f3.write(y1)
     f3.write(z1)
     f3.write(ab)
     f3.write(bc)
     f3.write(cd)
     f3.write(de)
     f3.write(ef)
     f3.close()     
def mental_health_display():
     f3=open("mental health.txt","r")
     s3=f3.readline()
     while s3:
          print(s3)
          s3=f3.readline()
     f3.close()
def signi_108():
     f5=open("signi108.txt","w")
     f5.write(a3)
     f5.write(fg)
     f5.write(gh)
     f5.write(hi)
     f5.write(ij)
     f5.write(jk)
     f5.write(kl)
     f5.close()     
def signi_108_display():
     f5=open("signi108.txt","r")
     s5=f5.readline()
     while s5:
          print(s5)
          s5=f5.readline()
     f5.close()     
def signi_med():
     f6=open("signimed.txt","w")
     f6.write(a4)
     f6.write(lm)
     f6.write(mn)
     f6.write(no)
     f6.write(op)
     f6.write(qr)
     f6.write(rs)
     f6.write(st)
     f6.write(tu)
     f6.close()     
def signi_med_display():
     f6=open("signimed.txt","r")
     s6=f6.readline()
     while s6:
          print(s6)
          s6=f6.readline()
     f6.close()
def chakra():
     f7=open("chakra.txt","w")
     f7.write(a5)
     f7.write(uv)
     f7.write(vw)
     f7.write(wx)
     f7.write(xy1)
     f7.write(yz)
     f7.write(za)
     f7.write(b1)
     f7.close()     
def chakra_display():
     f7=open("chakra.txt","r")
     s7=f7.readline()
     while s7:
          print(s7)
          s7=f7.readline()
     f7.close()        
#***********************************************BINARY FILE****************************************#
x="Q1.  ______________ is a huge and growing trend and, unlike the practice itself, it shows no signs of slowing down."
xx='MEDITATION'
y="Q2.Since 2012 the number of children meditating has increased more than ____%."
yy="80"
z="Q3.Meditation as a practice is thought to be around _______ years old."
zz="2600"
q="Q4. Meditation originated in______"
qq="INDIA"
r="Q5. Jainism, Taoism, and Confucianism propelled meditation techniques.(TRUE/FALSE)"
rr="TRUE"
p="Q6. SAHAJA is a type of _______ meditation?"
pp="YOGA"
xy="Q7. Meditation helps in self awareness.(TRUE/FALSE)"
aa="TRUE"
bb="Q8. which is the most ideal time to meditate?"
cc="SUNRISE"
dd="Q9. If you are quiet enough, you will hear the flow of the universe. You will feel its rhythm. Go with this flow. Happiness lies ahead. Meditation is key.WHO SAID THESE LINES?"
ee="LORD BUDDHA"
ff="Q10. Do meditation help in our spiritual growth?"
gg='YES'
import pickle
def binary_create():
     file_bin=open("MEDITATION.dat","wb")
     pickle.dump(x,file_bin)
     pickle.dump(y,file_bin)
     pickle.dump(z,file_bin)
     pickle.dump(q,file_bin)
     pickle.dump(r,file_bin)
     pickle.dump(p,file_bin)
     pickle.dump(xy,file_bin)
     pickle.dump(bb,file_bin)
     pickle.dump(dd,file_bin)
     pickle.dump(ff,file_bin)
     file_bin.close()
def unpickling():
     try:
          with open("MEDITATION.dat","rb") as f4:
               i=0
               while True:
                    data=pickle.load(f4)
                    print(data)
                    ans1=input("Answer 1. ")
                    if ans1==xx:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans2=input("Answer 2. ")
                    if ans2==yy:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans3=input("Answer 3. ")
                    if ans3==zz:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans4=input("Answer 4. ")
                    if ans4==qq:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans5=input("Answer 5. ")
                    if ans5==rr:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans6=input("Answer 6. ")
                    if ans6==pp:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans7=input("Answer 7. ")
                    if ans7==aa:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans8=input("Answer 8. ")
                    if ans8==cc:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans9=input("Answer 9. ")
                    if ans9==ee:
                         i+=1
                    else:
                         i+=0
                    
                    data=pickle.load(f4)
                    print(data)
                    ans10=input("Answer 10. ")
                    if ans10==gg:
                         i+=1
                    else:
                         i+=0
                    print("*"*160)
                    print("Your Score - " ,i)
                    if i<=3:
                         print("Poor Performance :( ")
                    elif i<=9:
                         print("Good Job!")
                    elif i==10:
                         print("Congratulations! Perfect Score.")
                    print("*"*160)
     except EOFError:
          pass 
#******************************************MAIN-PROGRAM*********************************************#
print("********MEDITATION,YOGA AND MENTAL HEALTH******")
print("1.LOGIN TO GENERATE AN ACCOUNT" ,"\n2.FACTS ON MEDITATION,YOGA AND MENTAL HEALTH" , "\n3.TEST YOURSELF WITH A QUIZ ON MEDITATION","\n4.STATISTICAL DATA \n5.LINKS FOR MORE INFORMATION\n6.EXIT")
while True:
     choice=int(input("Enter your choice - "))
     if choice==1:
          import mymodule
          mymodule.register_page()
          lino()
     elif choice==2:
          meditation()
          yoga()
          mental_health()
          signi_108()
          signi_med()
          chakra()
          print("(1).Facts on MEDITATION", "\n(2).Facts on YOGA","\n(3).Facts on MENTAL HEALTH","\n(4).Significance of number 108","\n(5).Significance of meditation in nature","\n(6).7 CHAKRAS OF HUMAN BODY","\n(7).EXIT")
          while True:
               inp=input("Enter your choice - ")
               if inp=="1":
                    lino()
                    meditation_display()
                    lino()
               elif inp=="2":
                    lino()
                    yoga_display()
                    lino()
               elif inp=="3":
                    lino()
                    mental_health_display()
                    lino()
               elif inp=="4":
                    lino()
                    signi_108_display()
                    lino()
               elif inp=="5":
                    lino()
                    signi_med_display()
                    lino()
               elif inp=="6":
                    lino()
                    chakra_display()
                    lino()
               elif inp=="7":
                    print("Exiting from sub-menu...")
                    print("Test your space knowledge with a small quiz using Binary File")
                    break
     elif choice==3:
          lino()
          binary_create()
          print("Remember: Write your answers in block letters")
          unpickling()
          lino()
     elif choice==4:
          lino()
          csvpro()
          lino()
     elif choice==5:
          lino()
          linkspro()
          lino()
     elif choice==6:
          print("EXITING.................STAY HAPPY (:->)")
          lino()
          break
     else:
          print("::::::::::wrong choice::::::::::::")
          
