# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#subloptを使用したグラフモジュール
def scatter_format(PARAM,Title,i,j,X,Y,COLOR,ALPHA,LABEL,MARKER,Name_Xaxis,Name_Yaxis,Xmin,Xmax,Xinterval,Ymin,Ymax,Yinterval,xLOG,yLOG,Grid):
    #RARAM:Parameter of graph / list [font,xdirection,ydirection,xwidth,ywidth,fontsize,linewidth]
    #Title:Graph title.number of title is i.
    #i:Number of Graph(<=9)
    #j:Number of Class
    #X:X-axis data ; [[x11,x12,x13,...x1j][x21,x22,x23,...,x2j]....[xi1,xi2,xi3,....,xij]]
    #X:Y-axis data ; [[y11,y12,y13,...y1j][y21,y22,y23,...,y2j]....[yi1,yi2,yi3,....,yij]]
    #ALPHA:透明度, numer of Aplha list is j
    #LABEL:label name,  number of label list is j
    #MARKER:maker name, number of marker list is j
    #Name_Xaxis:x-label,number is i
    #Name_Yaxis:y-label,number is i
    #Xmin,Ymin:min value, list length is i
    #Xmax,Ymin:max value, list length is i
    #Xinterval,Yinterval:interval value, list length is i
    #xLOG,yLOG:scale,list length is i, True or False
    #Grid:scale,list length is i, True or False
    plt.rcParams['font.family'] =PARAM[0]#使用するフォント
    plt.rcParams['xtick.direction'] = PARAM[1]#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = PARAM[2]#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = PARAM[3]#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = PARAM[4]#y軸主目盛り線の線幅
    plt.rcParams['font.size'] = PARAM[5] #フォントの大きさ
    plt.rcParams['axes.linewidth'] = PARAM[6]# 軸の線幅edge linewidth。囲みの太さ
    if(i<=1):
        for ii in range(i):
            plt.subplot(1,1,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    elif(i<=2):
        for ii in range(i):
            plt.subplot(1,2,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    elif(i<=3):
        for ii in range(i):
            plt.subplot(1,3,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    elif(i<=4):
        for ii in range(i):
            plt.subplot(2,2,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    elif(i<=6):
        for ii in range(i):
            plt.subplot(2,3,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    elif(i<=9):
        for ii in range(i):
            plt.subplot(3,3,ii+1)
            plt.title=Title[ii]
            Xi=X[ii]
            Yi=Y[ii]
            for jj in range(j):
                plt.scatter(x=Xi[jj],y=Yi[jj],c=COLOR[jj],maker=MARKER[jj],alpha=ALPHA[jj],edgecolors=COLOR[jj],label=LABEL[jj])
            plt.xlabel(Name_Xaxis[ii])
            plt.ylabel(Name_Yaxis[ii])
            plt.legend()
            plt.xlim(Xmin,Xmax,Xinterval)
            plt.ylim(Ymin,Ymax,Yinterval)
            if(xLOG[ii]==True):
                plt.xscale('log'):
            else:
                pass
            if(yLOG[ii]==True):
                plt.yscale('log'):
            else:
                pass
            if(Grid[ii]==True):
                plt.grid(which='major',color='black',linestyle='-')
                plt.grid(which='minor',color='grey',linestyle='-')
            else:
                pass
            plt.show()
    else:
        print("描画できるグラフ数を超えています。")
        print("You have ecxeeded the number you can draw!")
        pass



