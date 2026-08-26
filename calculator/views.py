from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        total_corn = float(request.POST.get('total_corn') or 0)
        total_soybeans = float(request.POST.get('total_soybeans') or 0)
        pop_corn = float(request.POST.get('pop_corn') or 0)
        pop_beans = float(request.POST.get('pop_beans') or 0)
        bushels_corn = float(request.POST.get('bushels_corn') or 0)
        bushels_beans = float(request.POST.get('bushels_beans') or 0)
        cost_seed = float(request.POST.get('cost_seed') or 0)
        cost_fert = float(request.POST.get('cost_fert') or 0)
        cost_rent = float(request.POST.get('cost_rent') or 0)
        cost_misc = float(request.POST.get('cost_misc') or 0)

        #Total income added together. Based on a set price currently.
        price_corn = 5.35
        price_beans = 11.50
        total_revenue = round((total_corn * bushels_corn * price_corn) \
                              + (total_soybeans * bushels_beans * price_beans), 2)
        #All costs added together.
        total_cost = round(cost_seed + cost_fert \
                      + cost_rent + cost_misc, 2)
        #Income minus costs.
        net_profit = round(total_revenue - total_cost, 2)

        #total_bushels = (total_corn * bushels_corn) + (total_soybeans * bushels_beans)
        #break_even_price = round(total_cost / total_bushels, 2) if total_bushels > 0 else 0

        #Finding our break even price per crop type (Corn and soybeans.)
        if total_corn + total_soybeans > 0:
            corn_percent = total_corn / (total_corn + total_soybeans)
            bean_percent = total_soybeans / (total_corn + total_soybeans)

            #Splitting costs by actual percentages.
            corn_costs = total_cost * corn_percent
            bean_costs = total_cost * bean_percent

            #Breaking even per crop:
            corn_break_even = round(corn_costs / (total_corn * bushels_corn), 2)\
                                     if total_corn * bushels_corn > 0 else 0
            bean_break_even = round(bean_costs / (total_soybeans * bushels_beans), 2)\
                                    if total_soybeans * bushels_beans > 0 else 0
            
            corn_profitable = price_corn > corn_break_even
            bean_profitable = price_beans > bean_break_even

        #Profitable indication.
        else:
            corn_break_even = 0
            bean_break_even = 0
            corn_profitable = False
            bean_profitable = False
        


        return render(request, 'calculator/home.html', 
                      # Inputs rendered
                    {'total_revenue': total_revenue,
                    'total_cost': total_cost,
                    'net_profit': net_profit,
                    'corn_break_even' : corn_break_even,
                    'bean_break_even' : bean_break_even,
                    'corn_profitable' : corn_profitable,
                    'bean_profitable' : bean_profitable,

                    # Input values to repopulate form
                    'total_corn': total_corn,
                    'total_soybeans': total_soybeans,
                    'pop_corn': pop_corn,
                    'pop_beans': pop_beans,
                    'bushels_corn': bushels_corn,
                    'bushels_beans': bushels_beans,
                    'cost_seed': cost_seed,
                    'cost_fert': cost_fert,
                    'cost_rent': cost_rent,
                    'cost_misc': cost_misc,
                    


                })
    else:
        return render(request, 'calculator/home.html')

