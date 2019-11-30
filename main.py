from math import e
import PySimpleGUI as sg
#tau =2.1
#T_1=4.8
#T_2=9.6
#T=0.36*(T_1+T_2)
#k=0.7
lay = [      
          [sg.Text('Introduceti datele de intrare')],      
           [sg.Text('tau '),sg.Input(size=(5,1))],  
           [sg.Text('T1  '),    sg.Input(size=(5,1))],
           [sg.Text('T2  '),    sg.Input(size=(5,1))],  
           [sg.Text('K   '),sg.Input(size=(5,1))],   
          [sg.Submit(button_text='Cavaler'), sg.Cancel()]      
         ]

window = sg.Window('Data Input ').Layout(lay)         
button, values = window.Read()
tau=float(values[0])
T_1=float(values[1])
T_2=float(values[2])
k=float(values[3])
T=0.36*(T_1+T_2)
print(f'T={T}')
T_extins = 0.22*(T_1+T_2)
b_0=k*(1+T_1/(T_2-T_1)-T_2/(T_2-T_1))
b_1=k*(2.72**(-T/T_1)+e**(-T/T_2)+(T_1/(T_2-T_1)*(1+e**(-T/T_2)))-(T_2/(T_2-T_1)*(1+e**(-T/T_1))))
b_2=k*((e**(-T/T_1))*(e**(-T/T_2))+(T_1/(T_2-T_1)*e**(-T/T_2))-T_2/(T_2-T_1)*e**(-T/T_2))
b_1=abs(b_1)
print('-'*7+'CALCULE PENTRU ALGORITM NORMAL'+'-'*7)
print ("b_0=%.4f" % b_0)
print(f'b_1={b_1}')
print ("b_2=%.16f" % b_2)
print('-'*5)
a_1 =e**(-T/T_1)+e**(-T/T_2)
a_2 =e**(-T/T_1)*e**(-T/T_2)
d=tau/T 
print(f'a_1={a_1}')
print(f'a_2={a_2}')
print(f'd={d}')
print('-'*5)
q_0=1/(b_1+b_2)
q_1=q_0*a_1
q_2=q_0*a_2
print(f'q_0={q_0}')
print(f'q_1={q_1}')
print(f'q_2={q_2}')
print('-'*5)
p_1=q_0*b_1
p_2=q_0*b_2
print(f'p_1={p_1}')
print(f'p_2={p_2}')
print('-'*41)
print('-'*7+'CALCULE PENTRU ALGORITM EXTINS'+'-'*7)
b_0_extins = 0
b_1_extins =k*(2.72**(-T_extins/T_1)+e**(-T_extins/T_2)+(T_1/(T_2-T_1)*(1+e**(-T_extins/T_2)))-(T_2/(T_2-T_1)*(1+e**(-T_extins/T_1)))) 
b_2_extins =k*((e**(-T_extins/T_1))*(e**(-T_extins/T_2))+(T_1/(T_2-T_1)*e**(-T_extins/T_2))-T_2/(T_2-T_1)*e**(-T_extins/T_2))
print ("b_0_extins=%.4f" % b_0_extins)
print(f'b_1_extins={b_1_extins}')
print ("b_2_extins=%.16f" % b_2_extins)
print('-'*5) 
a_1_extins =e**(-T_extins/T_1)+e**(-T_extins/T_2)
a_2_extins =e**(-T_extins/T_1)*e**(-T_extins/T_2)
d_extins=tau/T_extins 
print(f'a_1_extins={a_1_extins}')
print(f'a_2_extins={a_2_extins}')
print(f'd_extins={d_extins}')
print('-'*5)
q_0_extins=1/(b_1_extins+b_2_extins)
q_1_extins=q_0_extins*a_1_extins
q_2_extins=q_0_extins*a_2_extins
q_3_extins=-a_2_extins*(q_0_extins-1/2)
print(f'q_0_extins={q_0_extins}')
print(f'q_1_extins={q_1_extins}')
print(f'q_2_extins={q_2_extins}')
print(f'q_3_extins={q_3_extins}')
print('-'*5)
p_1_extins=q_0_extins*b_1_extins
p_2_extins=q_0_extins*(b_2_extins-b_1_extins)
p_3_extins=-b_2_extins*(q_0_extins-1/2)
print(f'p_1_extins={p_1_extins}')
print(f'p_2_extins={p_2_extins}')
print(f'p_3_extins={p_3_extins}')
print('-'*41)


length = 7
print(f'H_d(z)=z^-{d} * ( {b_0}-z^-1*{b_1}-{b_2}*z^-2 ) /1-{a_1}z^-1+{a_2}*z^-2')

layout = [      
          [sg.Text('CALCULE PENTRU ALGORITM NORMAL')],      
         [sg.Text('b0', size=(15, 1)), sg.Input("%.4f" % b_0, size=(length, 1))],      
          [sg.Text('b1', size=(15, 1)), sg.Input("%.4f" % b_1, size=(length, 1))],        
          [sg.Text('b2', size=(15, 1)), sg.Input("%.4f" % b_2, size=(length, 1))], 
          [sg.Text('a1', size=(15, 1)), sg.Input("%.4f" % a_1, size=(length, 1))],
           [sg.Text('a2', size=(15, 1)), sg.Input("%.4f" % a_2, size=(length, 1))],      
          [sg.Text('d', size=(15, 1)), sg.Input("%.4f" % d, size=(length, 1))],        
          [sg.Text('b2', size=(15, 1)), sg.Input("%.4f" % b_2, size=(length, 1))],
           [sg.Text('q0', size=(15, 1)), sg.Input("%.4f" % q_0, size=(length, 1))],      
          [sg.Text('q1', size=(15, 1)), sg.Input("%.4f" % q_1, size=(length, 1))],        
          [sg.Text('q2', size=(15, 1)), sg.Input("%.4f" % q_2, size=(length, 1))],  
          [sg.Text('CALCULE PENTRU ALGORITM EXTINS')],      
          [sg.Text('b0', size=(15, 1)), sg.Input("%.4f" % b_0_extins, size=(length, 1))],      
          [sg.Text('b1', size=(15, 1)), sg.Input("%.4f" % b_1_extins, size=(length, 1))],        
          [sg.Text('b2', size=(15, 1)), sg.Input("%.4f" % b_2_extins, size=(length, 1))], 
          [sg.Text('a1', size=(15, 1)), sg.Input("%.4f" % a_1_extins, size=(length, 1))],
           [sg.Text('a2', size=(15, 1)), sg.Input("%.4f" % a_2_extins, size=(length, 1))],      
          [sg.Text('d', size=(15, 1)), sg.Input("%.4f" % d_extins, size=(length, 1))],        
          [sg.Text('b2', size=(15, 1)), sg.Input("%.4f" % b_2_extins, size=(length, 1))],
           [sg.Text('q0', size=(15, 1)), sg.Input("%.4f" % q_0_extins, size=(length, 1))],      
          [sg.Text('q1', size=(15, 1)), sg.Input("%.4f" % q_1_extins, size=(length, 1))],        
          [sg.Text('q2', size=(15, 1)), sg.Input("%.4f" % q_2_extins, size=(length, 1))],           
          [sg.Submit(), sg.Cancel()]      
         ]

window = sg.Window('OUT_DATA').Layout(layout)         
button, values = window.Read()

print(button, values[0], values[1], values[2])
