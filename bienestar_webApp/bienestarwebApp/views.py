from django.shortcuts import render, get_object_or_404, redirect
import mercadopago
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import datetime
from .models import Paginas, Faqs, Entradas, Reviews, Planes, Aviso
from ventas.models import Venta
from .forms import VentasFormulario
from web_api.api import get_offerings, check_cobertura, get_preferences, get_profile_data_clean, get_all_mb_plans, get_all_mifi_plans, get_offer_id, get_offer_price, get_users_length, getUserByNumber, send_subscriptions
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import json
import requests


# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("PROD_ACCESS_TOKEN")

# Create your views here.


def intro(request):

    if request.method == 'POST':
        print("[Info][Landing.Intro] Entring the post...")

        name = ""
        number = ""
        email = ""

        if request.POST.get('name'):
            name = request.POST.get('name')
        if request.POST.get('cel'):
            number = request.POST.get('cel')
        if request.POST.get('sub_email'):
            email = request.POST.get('sub_email')

        # Guardar en BD
        prospect_dict = {
            "name" : name,
            "number" : number,
            "email" : email
        }

        send_subscriptions(prospect_dict)


    # call traductor
    planesMB = get_offerings("IB-MB")
    planesMB = json.loads(planesMB)

    # cantidad de usuarios
    reviews_ = Reviews.objects.all()

    # Info para app usuarios
    usersLen = get_users_length()
    print(type(usersLen))
    print(int(usersLen))
    user_Len = int(usersLen)
    user_Len = usersLen / 10 

    usr_descargas = 25
    usr_clientesSatisfechos = 100
    usr_estados = 15

    Faqs_ = Faqs.objects.all()[:5]
    Entradas_ = Entradas.objects.all()
    
    print(user_Len)

    return render(request, 'bienestarwebApp/index.html',
                  {
                      "planes": planesMB,
                      'usersLen': usersLen,
                      'usr_descargas' : usr_descargas,
                      'usr_clientesSatisfechos' : usr_clientesSatisfechos,
                      'usr_estados' : usr_estados,
                      'user_Len' : int(user_Len),
                      "Faqs": Faqs_,
                      "Entradas" : Entradas_,
                      "reviews" : reviews_,
                  })


def avisos_privacidad(request):

    avisos_ = Aviso.objects.all()
    return render(request, "bienestarwebApp/aviso/aviso.html", {"avisos": avisos_ })

def cobertura(request):
    #return render(request, "bienestarwebApp/HBB/cobertura.html")
    return render(request, "bienestarwebApp/paginas/cobertura.html")

def portabilidad(request):
    return render(request, "bienestarwebApp/paginas/portabilidad.html")

def compatibilidad(request):
    return render(request, "bienestarwebApp/paginas/compatibilidad.html")

def paginas(request, page_name):
    pags = get_object_or_404(Paginas, titulo=page_name)

    privacidad_content = Paginas.objects.exclude(titulo__contains="_")

    context = {
        "pags": pags
    }

    if 'aviso_privacidad' in page_name:
        context["privacidad"] = privacidad_content

    return render(request, "bienestarwebApp/paginas/paginas.html", context)

def faqs(request):
    Faqs_ = Faqs.objects.all()
    context = {
        "Faqs": Faqs_
    }

    return render(request, "bienestarwebApp/faqs/faqs.html", context)


def distribuidores(request):

    if settings.DEBUG:
        host = "127.0.0.1:8000"
    else:
        host = "jrmovil.pythonanywhere.com"

    return render(request, "bienestarwebApp/distribuidores/distribuidoresForm.html")

# Just demo
@csrf_protect
def mercado_pago_api(request):

    if settings.DEBUG:
        host = "127.0.0.1:8000"
    else:
        host = "jrmovil.pythonanywhere.com"

    if request.method == 'POST':

        print("[Info] Web Mercado pago Init...  ")
        paquete = None

        if "empty" not in request.POST.get('dropdownMB'):
            paquete = request.POST.get('dropdownMB')
        if "empty" not in request.POST.get('dropdownMIFI'):
            paquete = request.POST.get('dropdownMIFI')

        cel = request.POST.get('idSubscriber')
        # sub_email = request.POST.get('email')

        # print(request.POST)
        if paquete:
            print("[Info][mercado_pago_api] Preparing data for recharge.")

            planId = get_offer_id(paquete)
            cliente = getUserByNumber(cel)
            email = "anonymous@gmail.com"

            if(cliente): email = cliente.user_number 

            
            price = get_offer_price(planId)
            # Get Preference ID
            raw = {
                "title": paquete,
                "unit_price": price,
                "idSubscriber": cel,
                "email": email
            }

            preference_mo = get_preferences(raw)
            print(' ***** payment response ****')
            print(preference_mo)

            #return HttpResponseRedirect(preference_mo["init_point"])
            return render(request, 'bienestarwebApp/recargas/mp_iframe.html', {"iframe_url" : preference_mo["init_point"]})
        
        # Search for JRmóvil
        uf_response = get_profile_data_clean(cel)
        if uf_response:
            return HttpResponseRedirect("http://" + host + "/recargas?" + cel + "ok")
        else:
            return HttpResponseRedirect("http://" + host + "/recargas?" + cel + "denied")

    
    allMB = get_all_mb_plans()
    allMifi = get_all_mifi_plans()
    

    return render(request, 'bienestarwebApp/recargas/recargas.html', {
        "allMB" : allMB,
        "allMifi" : allMifi
        })


def consultas(request):
    context = {}

    if request.method == 'POST':

        print("[Info] Web Consulta saldo Init...  ")
        cel = request.POST.get('idSubscriber')
        # sub_email = request.POST.get('email')

        print("[Info][mercado_pago_api] Searching client..")  
        # Search for JRmóvil
        uf_response = get_profile_data_clean(cel)
        print("******************** uf_response ")
        #data = json.load(uf_response)
        print(uf_response["offeringId"])
        context["number"] = cel
        context["paquete_name"] = uf_response["offeringName"]
        context["expireDate"] = uf_response["expireDate"]
        context["effectiveDate"] = uf_response["effectiveDate"]
        context["initialDataAmt"] = uf_response["initialDataAmt"]
        context["unusedDataAmt"] = uf_response["unusedDataAmt"]
        context["totalMin"] = uf_response["totalMin"]
        context["totalUnusedMin"] = uf_response["totalUnusedMin"]
        context["totalSMS"] = uf_response["totalSMS"]
        context["totalUnusedSMS"] = uf_response["totalUnusedSMS"]
      

    return render(request, 'bienestarwebApp/consultas/index.html', context)

def contact(request):
    return render(request, "bienestarwebApp/contact/contact.html")

def about(request):
    return render(request, "bienestarwebApp/about/about.html")

def maps_view(request):       
    return render(request, 'googleMap.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

def autocomplete(request):       
    return render(request, 'googleMap.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

def hbb(request):
    responseHbb = None
    cobertura = False
    msgResponse = None
    planes = get_offerings("HBB")
    planes = json.loads(planes)


    if request.POST.get:
        lat = request.POST.get('latitud')
        lng = request.POST.get('longitud')
        direccion = request.POST.get('autocomplete')

        if lat and lng:
            responseHbb = check_cobertura(lat, lng)

            if "Without Coverage" in responseHbb:
                responseHbb = "Aún estamos trabajando duro para llevar la cobertura hasta donde estás"   
            else:
                responseHbb = "¡Ya contamos con cobertura en donde tú estás!"
                cobertura = True

            msgResponse = "HBBServiceOn"

            # Limpiar los datos de request.POST
            request.POST = request.POST.dict()
            if cobertura:
                return redirect("hbb_result_ok")
            else:
                return redirect("hbb_result_fail")


    return render(request, "bienestarwebApp/HBB.html", {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY, 
        'responseHbb' : responseHbb,
        'cobertura':cobertura,
        'msgResponse' : msgResponse,
        'planes' : planes
    })

def hbb_result_fail(request):       
    return render(request, "bienestarwebApp/HBB/resultFail.html")

def hbb_result_ok(request):       
    return render(request, "bienestarwebApp/HBB/resultOk.html")

def redireccion_recarga(request):
    return redirect('https://jrmovil.pythonanywhere.com/recargas')

def compraChip(request):
    base_precio = 100
    shipment = 30
    if request.method == "POST":
        form = VentasFormulario(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            payload = {
                'nombre':form.cleaned_data['nombre'],
                'apellido':form.cleaned_data['apellido'],
                'email':form.cleaned_data['email'],
                'celular':form.cleaned_data['celular'],
                'calle':form.cleaned_data['calle'],
                'numExt':form.cleaned_data['no_ext'],
                'numInt':form.cleaned_data['no_int'],
                'colonia':form.cleaned_data['colonia'],
                'codigo_postal':form.cleaned_data['codigo_postal'],
                'estado':form.cleaned_data['estado'],
                'municipio':form.cleaned_data['municipio'],
                'referencias':form.cleaned_data['referencias'],
                'precio':form.cleaned_data['precio'],
                'cantidad':form.cleaned_data['cantidad'],
                'aceptar_aviso':form.cleaned_data['aceptar_aviso']
            }
            post.save()

            print(f"[Info] Web Pasarela de pago iniciada Init... {payload['nombre']} {payload['email']}")
            etiqueta_precio = dict(Venta.PLANES_CHOICES).get(payload["precio"])
            if payload["cantidad"] > 1 : precio = base_precio * payload["cantidad"] 
            else: precio = base_precio
            
            if len(payload["numInt"]) == 0 or payload["numInt"] == None:
                numInt = "n/a"
            else: numInt = payload["numInt"]
            
            precio += shipment
            print(f"[Info] precio variable... ", precio)
            raw = {
                "nombre": payload["nombre"],
                "apellido": payload["apellido"],
                "email": payload["email"],
                "celular": payload["celular"],
                "calle": payload["calle"],
                "numExt": payload["numExt"],
                "numInt": numInt,
                "colonia": payload["colonia"],
                "cpostal": payload["codigo_postal"],
                "estado": payload["estado"],
                "municipio": payload["municipio"],
                "refDomicilio": payload["referencias"],
                #"precio": payload["precio"],
                "precio": payload["precio"],
                "cantidad": payload["cantidad"],
                "producto": etiqueta_precio,
                "aceptar_aviso": payload["aceptar_aviso"],
            }

            print("Payload compra SIM", raw)
           
            url = "https://jrmovil.pythonanywhere.com/IBienestar-services/2.0/api/sim-purchase/"
            response = requests.post(url, data=raw)
            
            if response.status_code == 201:
                print("Response compra SIM --->>>>> ", response.json()['purchase_response']['Gateaway_link'])
                print("SIM solicitada correctamente")
            else:
                try:                    
                    raise Exception("Error al solicitar tu sim",response.status_code)
                except Exception as e:
                    return HttpResponse(f"Se produjo un error: {str(e)}")

            #return HttpResponseRedirect(preference_mo["init_point"])
            return render(request, 'bienestarwebApp/compraChip/mo_iframe.html', {"iframe_url" : response.json()['purchase_response']['Gateaway_link']})

            #return redirect('pago')
    else:
        form = VentasFormulario()
    return render(request, "bienestarwebApp/compraChip/compraChipForm.html", {'form': form})

def paymentChip(request):
    return render(request,"bienestarwebApp/compraChip/paymentChip.html")


def enviar_imei(request):
    if request.method == 'POST':
        form = ImeiForm(request.POST)
        if form.is_valid():
            imei = form.cleaned_data['imei']
            return render(request, 'compatibilidad.html', {'form': form, 'imei_enviado': imei})
    else:
        form = ImeiForm()

    return render(request, 'compatibilidad.html', {'form': form})