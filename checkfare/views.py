from django.shortcuts import render
from setfare.models import bus_fare, bus_details, bus_route
# Create your views here.
def index(request):

    
    return render(request, "index.html")


def confirm_bus(request):
    get_lisence_no_name = request.POST.get('lisence_no')
    name = bus_details.objects.filter(lisence_no= get_lisence_no_name)

    details ={
        'lisence_n':get_lisence_no_name,
        'busName': name,
    }
    return render(request, 'confirm_bus.html', details)

def give_destination(request):
    get_lisence_no = request.POST.get('lisence_no')
    busName = request.POST.get('Bus_name')
    route_details = bus_route.objects.filter(lisence_no= get_lisence_no)
    available_routes ={
        'lisence_n':get_lisence_no,
        'b_name' : busName,
        'rt' :route_details,
    }

    return render(request, "destination.html", available_routes)




def calcualte_fare(request):
    lisence_number = request.POST.get('lisence_no')
    starting_point = request.POST.get('pickup_point')
    ending_point = request.POST.get('destination_point')

    bus_fare_cal = bus_fare.objects.filter(lisence_no= lisence_number, start_point=starting_point, end_point = ending_point)
    
    final_fare = {
        'pickup' : starting_point,
        'destination' : ending_point,
        'payable' : bus_fare_cal
    }
    
    return render(request, "Fare.html", final_fare)