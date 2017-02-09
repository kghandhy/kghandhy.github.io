'''Shows the growth of 12 randomly selected YouTubers from October 2015 until now, January 2017'''
import matplotlib.pyplot as plt

plt.figure

 

#sets number of views from october 2015 - january 2017 for each specific YouTuber from a csv file

datafile = open('data.csv','r')
data = datafile.readlines()

rikki_poynter=[]
hey_im_natalia=[]
itsamemlyo = []
arkas = []
mister_game_craft = []
bj_produces = []
thekingofhatevlogs = []
wwestevo07 = []
jordan_doww = []
kevinbruek = []
haloqg = []
usctmb = []


for line in data[1:]: # Omit header lines
    youtub1, youtub2, youtub3, youtub4, youtub5, youtub6, youtub7, youtub8, youtub9, youtub10, youtub11, youtub12 = line.split(',')
    rikki_poynter.append(youtub1)
    hey_im_natalia.append(youtub2)
    itsamemlyo.append(youtub3)
    arkas.append(youtub4)
    mister_game_craft.append(youtub5)
    bj_produces.append(youtub6)
    thekingofhatevlogs.append(youtub7)
    wwestevo07.append(youtub8)
    jordan_doww.append(youtub9)
    kevinbruek.append(youtub10)
    haloqg.append(youtub11)
    usctmb.append(youtub12)

x_axis_values_months = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

tick_spacing = 1
#plots growth for each YouTuber

plt.plot(rikki_poynter, label="Rikki Poynter")

plt.plot(hey_im_natalia, label="Hey I'm Natalia")

plt.plot(itsamemlyo, label="Itsamemlyo")

plt.plot(arkas, label="Arkas")

plt.plot(mister_game_craft, label="MisterGameCraft")

plt.plot(bj_produces, label="Bj Produces")

plt.plot(thekingofhatevlogs, label="Thekingofhatevlogs")

plt.plot(wwestevo07, label="Wwestevo07")

plt.plot(jordan_doww, label="JordanDoww")

plt.plot(kevinbruek, label="Kevinbruek")

plt.plot(haloqg, label="Haloqg")

plt.plot(usctmb, label="USCTMB")

 

#label x-axis, y-axis, and entire plot

plt.xlabel("Months(October 2015 - January 2017)")

plt.ylabel("Number Of Views")

plt.title ("Rate Of Growth For People Under 100k Subs\n (From When YouTube Red Launched)")





#limites the range of x and y axis

plt.xlim(0, 15)

plt.ylim(0, 17900000) 

plt.plot(figsize=(12,3))

 

#creates legend that correlates color with a certain YouTuber

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,], ['Oct 2015', 'Nov 2015', 'Dec 2015', 'Jan 2016', 'Feb 2016', 'Mar 2016', 'April 2016', 'May 2016', 'June 2016', 'July 2016', 'Aug 2016', 'Sept 2016', 'Oct 2016', 'Nov 2016', 'Dec 2016', 'Jan 2017'])


plt.legend(loc="upper left", fontsize = 'x-small')

plt.show()