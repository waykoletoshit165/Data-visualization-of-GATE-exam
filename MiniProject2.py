from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

choice=input("In which type, you want data('tabular','pie-chart'): ")

if choice=='tabular':
    distrubution={"Subjects":["Production","IM & OR","Fluid mechanics & Turbo machinery","Heat Transfer","Thermodynamics",
                                    "Strength of Materials","Machine Design","Theory of Machine","Engineering Mechanics","Material Science",
                                    "Engineering Mathematics","Genral Aptitude"],
                        "marks in 2019":[20,5,9,9,12,10,5,12,5,4,19,20],
                        "marks in 2020":[18,8,10,6,15,9,6,9,5,4,20,20],
                        "marks in 2021":[20,9,12,7,13,8,6,11,5,2,17,20],
                        "marks in 2022":[17,10,10,11,9,8,3,10,9,5,18,20]
                        }
    df=pd.DataFrame(distrubution)
    df.index=np.arange(1,len(df)+1)
    print(df)
elif choice=='pie-chart':
    No_Of_Questions=[75,32,41,33,49,35,20,42,24,15,74,80]
    Subjects=["Production","IM & OR","Fluid mechanics & Turbo machinery","Heat Transfer","Thermodynamics","Strength of Materials","Machine Design","Theory of Machine","Engineering Mechanics","Material Science","Engineering Mathematics","Genral Aptitude"]
    cols=['b','g','r','c','m','y','tab:brown','C0','tab:pink','tab:purple','tab:gray','tab:orange']
    plt.pie(No_Of_Questions, labels=Subjects, colors=cols, startangle=90, shadow=True, explode=(0,0,0,0,0,0,0,0,0,0,0,0.1),autopct='%1.1f%%')
    plt.title('Pie graph')
    plt.show()
else:
    print("You did something wrong.")
