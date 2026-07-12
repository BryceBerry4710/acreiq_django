from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        total_corn = float(request.POST.get('total_corn') or 0)
        total_soybeans = float(request.POST.get('total_soybeans') or 0)
        bushels_corn = float(request.POST.get('bushels_corn') or 0)
        bushels_beans = float(request.POST.get('bushels_beans') or 0)
        cost_seed = float(request.POST.get('cost_seed') or 0)
        cost_fert = float(request.POST.get('cost_fert') or 0)
        cost_rent = float(request.POST.get('cost_rent') or 0)
        cost_misc = float(request.POST.get('cost_misc') or 0)


        price_corn = 5.35
        price_beans = 11.50
        total_revenue = round(total_corn * bushels_corn * price_corn) \
            + (total_soybeans * bushels_beans * price_beans, 2)
        
        total_cost = round(cost_seed + cost_fert \
                      + cost_rent + cost_misc, 2)
        
        net_proft = round(total_revenue - total_cost, 2)


        return render(request, 'calculator/home.html', 
                    {'total_revenue': total_revenue,
                    'total_cost': total_cost,
                    'net_profit': net_proft,
                })
    else:
        return render(request, 'calculator/home.html')

