from flask import Flask, render_template, request, redirect, url_for, flash, session
import locale
try:
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    
import pandas as pd
master_file=pd.read_excel('master.xlsx')
app = Flask(__name__)



def air(weight,destination):
    # first_air_slab=250
    # part_air_slab=250
    air_tar=0
    air_gst=0
    air_tar_total=0
    print(destination)
    destination=str(destination)
    first_air_price=master_file[master_file['Destination']==destination]['air1'].iloc[0]
    part_air_price=master_file[master_file['Destination']==destination]['air2'].iloc[0]

    max_wt=int(master_file[master_file['Destination']==destination]['air_wt'].iloc[0])
    if max_wt==0:
        air_tar='No Service'
        air_gst='No Service'
        air_tar_total='No Service'
    elif weight>max_wt:
        air_tar='Max Weight is '+str(max_wt)+' Grams'
        air_gst='Max Weight is '+str(max_wt)+' Grams'
        air_tar_total='Max Weight is '+str(max_wt)+' Grams'
    else:
        if weight<=250:
            air_tar=first_air_price
        else:
            if (weight-250)%250==0:
                air_tar=(first_air_price)+(((weight-250)//250)*part_air_price)
            else:
                air_tar=(first_air_price)+((1+((weight-250)//250))*part_air_price)
        air_gst=air_tar*18/100
        air_tar_total=air_tar+air_gst
        air_tar='₹ '+locale.format_string("%0.0f", round(air_tar), grouping=True)
        air_gst='₹ '+locale.format_string("%0.0f", air_gst, grouping=True)
        air_tar_total='₹ '+locale.format_string("%0.0f", air_tar_total, grouping=True)

    list=[air_tar,air_gst,air_tar_total]
    return list

def ems(weight,destination):
    # first_ems_slab=250
    # part_ems_slab=250
    ems_tar=0
    ems_gst=0
    ems_tar_total=0
    first_ems_price=master_file[master_file['Destination']==destination]['ems1'].iloc[0]
    part_ems_price=master_file[master_file['Destination']==destination]['ems2'].iloc[0]

    max_wt=int(master_file[master_file['Destination']==destination]['ems_wt'].iloc[0])
    if max_wt==0:
        ems_tar='No Service'
        ems_gst='No Service'
        ems_tar_total='No Service'
    elif weight>max_wt:
        ems_tar='Max Weight is '+str(max_wt)+' Grams'
        ems_gst='Max Weight is '+str(max_wt)+' Grams'
        ems_tar_total='Max Weight is '+str(max_wt)+' Grams'
    else:
        if weight<=250:
            ems_tar=first_ems_price
        else:
            if (weight-250)%250 == 0:
                ems_tar=(first_ems_price)+(((weight-250)//250)*part_ems_price)
            else:    
                ems_tar=(first_ems_price)+((1+((weight-250)//250))*part_ems_price)
        ems_gst=ems_tar*18/100
        ems_tar_total=ems_tar+ems_gst
        ems_tar='₹ '+locale.format_string("%0.0f", round(ems_tar), grouping=True)
        ems_gst='₹ '+locale.format_string("%0.0f", ems_gst, grouping=True)
        ems_tar_total='₹ '+locale.format_string("%0.0f", ems_tar_total, grouping=True)
    list=[ems_tar,ems_gst,ems_tar_total]
    return list

def itps(weight,destination):
    # first_itps_slab=50
    # part_itps_slab=50
    itps_tar=0
    itps_gst=0
    itps_tar_total=0
    first_itps_price=master_file[master_file['Destination']==destination]['itps1'].iloc[0]
    part_itps_price=master_file[master_file['Destination']==destination]['itps2'].iloc[0]

    max_wt=int(master_file[master_file['Destination']==destination]['itps_wt'].iloc[0])
    if max_wt==0:
        itps_tar='No Service'
        itps_gst='No Service'
        itps_tar_total='No Service'
    elif weight>max_wt:
        itps_tar='Max Weight is '+str(max_wt)+' Grams'
        itps_gst='Max Weight is '+str(max_wt)+' Grams'
        itps_tar_total='Max Weight is '+str(max_wt)+' Grams'
    else:
        if weight<=50:
            itps_tar=first_itps_price
        else:
            if (weight-50)%50==0:
                itps_tar=int(first_itps_price)+(((weight-50)//50)*part_itps_price)
            else:
                itps_tar=int(first_itps_price)+((1+((weight-50)//50))*part_itps_price)
        itps_gst=itps_tar*18/100
        itps_tar_total=itps_tar+itps_gst
        itps_tar='₹ '+locale.format_string("%0.0f", round(itps_tar), grouping=True)
        itps_gst='₹ '+locale.format_string("%0.0f", itps_gst, grouping=True)
        itps_tar_total='₹ '+locale.format_string("%0.0f", itps_tar_total, grouping=True)
    list=[itps_tar,itps_gst,itps_tar_total]
    return list

def rl(weight,destination):
    # first_rl_slab=20
    # part_rl_slab=20
    rl_tar=0
    rl_gst=0
    rl_tar_total=0
    first_rl_price=master_file[master_file['Destination']==destination]['rl1'].iloc[0]
    part_rl_price=master_file[master_file['Destination']==destination]['rl2'].iloc[0]

    max_wt=int(master_file[master_file['Destination']==destination]['rl_wt'].iloc[0])
    if max_wt==0:
        rl_tar='No Service'
        rl_gst='No Service'
        rl_tar_total='No Service'
    elif weight>max_wt:
        rl_tar='Max Weight is '+str(max_wt)+' Grams'
        rl_gst='Max Weight is '+str(max_wt)+' Grams'
        rl_tar_total='Max Weight is '+str(max_wt)+' Grams'
    else:
        if weight<=20:
            rl_tar=first_rl_price
        else:
            if (weight-20)%20==0:
                rl_tar=(first_rl_price)+(((weight-20)//20)*part_rl_price)
            else:
                rl_tar=(first_rl_price)+((1+((weight-20)//20))*part_rl_price)
        rl_gst=rl_tar*18/100
        rl_tar_total=rl_tar+rl_gst
        rl_tar='₹ '+locale.format_string("%0.0f", round(rl_tar), grouping=True)
        rl_gst='₹ '+locale.format_string("%0.0f", rl_gst, grouping=True)
        rl_tar_total='₹ '+locale.format_string("%0.0f", rl_tar_total, grouping=True)
    # list=[f'₹{rl_tar}',f'₹{rl_gst}',f'₹{rl_tar_total}']
    list=[rl_tar,rl_gst,rl_tar_total]
    return list

@app.route('/')
def home():
    destinations=master_file['Destination']
    return render_template('home.html',destinations=destinations)
    
@app.route('/tariff', methods=['POST'])
def tariff():
    if request.method == 'POST':
        destinations=master_file['Destination']
        destination1=str(request.form['destination'])
        print(destination1)
        weight=int(request.form['weight'])
        [air_tar, air_gst, air_tar_total]=air(weight,destination1)
        print(air(weight,destination1))
        [ems_tar, ems_gst, ems_tar_total]=ems(weight,destination1)
        [itps_tar,itps_gst,itps_tar_total]=itps(weight,destination1)
        print(itps(weight,destination1))

        [rl_tar, rl_gst, rl_tar_total]=rl(weight,destination1)

        return render_template('tariff.html',destinations=destinations,destination1=destination1,weight=weight,air_tar=air_tar,air_gst=air_gst,air_tar_total=air_tar_total,ems_tar=ems_tar, ems_gst=ems_gst, ems_tar_total=ems_tar_total,itps_tar=itps_tar,itps_gst=itps_gst,itps_tar_total=itps_tar_total,rl_tar=rl_tar, rl_gst=rl_gst, rl_tar_total=rl_tar_total)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
