import pandas, numpy,pygal
from matplotlib import  pyplot as plt
from matplotlib import style
from project_module import project
data_frame = pandas.read_csv('D://UIT//2ndSemester//ObjectOrientedProgramming//OOP Final Project//vgsales_ext.csv')
def main():
    x3 = project.fill_missing_year(summed_genre_sales('X360'))
    ps4 = project.fill_missing_year(summed_genre_sales('PS4'))
    ps3 = project.fill_missing_year(summed_genre_sales('PS3'))
    ps2 = project.fill_missing_year(summed_genre_sales('PS2'))
    wii = project.fill_missing_year(summed_genre_sales('Wii'))
    nes = project.fill_missing_year(summed_genre_sales('NES'))
    G = project.fill_missing_year(summed_genre_sales('G'))
    DS = project.fill_missing_year(summed_genre_sales('DS'))
    snes = project.fill_missing_year(summed_genre_sales('SNES'))
    gba = project.fill_missing_year(summed_genre_sales('GBA'))
    ds3 = project.fill_missing_year(summed_genre_sales('3DS'))
    ng4 = project.fill_missing_year(summed_genre_sales('N64'))
    pc = project.fill_missing_year(summed_genre_sales('PC'))
    ps = project.fill_missing_year(summed_genre_sales('PS'))
    psp = project.fill_missing_year(summed_genre_sales('PSP'))
    xb1 = project.fill_missing_year(summed_genre_sales('XBoxOne'))
    wiiu = project.fill_missing_year(summed_genre_sales('WiiU'))
    gc = project.fill_missing_year(summed_genre_sales('GC'))
    gen = project.fill_missing_year(summed_genre_sales('GEN'))
    dc = project.fill_missing_year(summed_genre_sales('DC'))
    psv = project.fill_missing_year(summed_genre_sales('PSV'))
    sat = project.fill_missing_year(summed_genre_sales('SAT'))
    scd = project.fill_missing_year(summed_genre_sales('SCD'))
    ws = project.fill_missing_year(summed_genre_sales('WS'))
    ng = project.fill_missing_year(summed_genre_sales('NG'))
    tg16 = project.fill_missing_year(summed_genre_sales('TG16'))
    dg3 = project.fill_missing_year(summed_genre_sales('3DG'))
    do3 = project.fill_missing_year(summed_genre_sales('3DO'))
    gg = project.fill_missing_year(summed_genre_sales('GG'))
    pcfx = project.fill_missing_year(summed_genre_sales('PCFX'))

    create_chart(x3, ps4, ps3, ps2,wii,nes,G,DS,snes,gba,ds3,ng4,pc,ps,psp,xb1,wiiu,gc,gen,dc,psv,sat,scd,ws,ng,tg16,dg3,do3,gg,pcfx)

def summed_genre_sales(genre):
    """ This Function for Summed Sales of Years in Zone """
    genre_sales = []
    all_genre_list = numpy.array(data_frame.groupby(['Year', 'Platform'], as_index=False).sum()[['Year', 'Platform', 'Global_Sales']]).tolist()
    for i in all_genre_list:
        selected = [i[0], i[2]]
        if i[1] == genre:
            genre_sales.append(selected)
    return genre_sales


def create_chart(a, b, c, d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad):
    """ This Function for create chart """

    chart = pygal.Line()
    chart.x_title = 'Year'
    chart.y_title = 'Sales'

    chart.x_labels = map(str, range(1980, 2016))

    chart.add("X360", [i[1] for i in a])
    chart.add("PS4", [i[1] for i in b])
    chart.add("PS3", [i[1] for i in c])
    chart.add("PS2", [i[1] for i in d])
    chart.add("WII", [i[1] for i in e])
    chart.add("NES", [i[1] for i in f])
    chart.add("G", [i[1] for i in g])
    chart.add("DS", [i[1] for i in h])
    chart.add("SNES", [i[1] for i in i])
    chart.add("GBA", [i[1] for i in j])
    chart.add("3DS", [i[1] for i in k])
    chart.add("NG4", [i[1] for i in l])
    chart.add("PC", [i[1] for i in m])
    chart.add("PS", [i[1] for i in n])
    chart.add("PSP", [i[1] for i in o])
    chart.add("XBox1", [i[1] for i in p])
    chart.add("WIIU", [i[1] for i in q])
    chart.add("GC", [i[1] for i in r])
    chart.add("GEN", [i[1] for i in s])
    chart.add("DC", [i[1] for i in t])
    chart.add("PSV", [i[1] for i in u])
    chart.add("SAT", [i[1] for i in v])
    chart.add("SCD", [i[1] for i in w])
    chart.add("WS", [i[1] for i in x])
    chart.add("NG", [i[1] for i in y])
    chart.add("TG16", [i[1] for i in z])
    chart.add("3DG", [i[1] for i in aa])
    chart.add("3DO", [i[1] for i in ab])
    chart.add("GG", [i[1] for i in ac])
    chart.add("PCFX", [i[1] for i in ad])
    chart.render_in_browser()


main()
