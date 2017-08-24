from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *
from mapping.models import Person,Car,Student,Department,Game,Athlete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer,GameSerializer,AthleteSerializer
from rest_framework.parsers import JSONParser



#lists all registrations or create a new one
#registrationurl/
class RegistrationList(APIView):
    def get(self,request):
        registrations=Registration.objects.all()
        serializer=RegistrationSerializer(registrations,many=True)
        return Response(serializer.data)
    def post(self):
        pass

#lists all game or create a new one
#gameurl/

class GameList(APIView):
    def get(self,request):
        games=Game.objects.all()
        serializer=GameSerializer(games,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
#----------
#----------

class GameDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self,pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404


    def get(self,request,pk):
        game=self.get_object(pk)
        serializer=GameSerializer(game)
        return Response(serializer.data)

    def put(self,request,pk):
        game=self.get_object(pk)
        serializer=GameSerializer(game,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        game=self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#----------
#----------


#lists all athlete or create a new one
#athleteurl/
class AthleteList(APIView):
    def get(self,request):
        athletes=Athlete.objects.all()
        serializer=AthleteSerializer(athletes,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = AthleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#-----------
#-----------
class AthleteDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self,pk):
        try:
            return Athlete.objects.get(pk=pk)
        except Athlete.DoesNotExist:
            raise Http404


    def get(self,request,pk):
        athlete=self.get_object(pk)
        serializer=AthleteSerializer(athlete)
        return Response(serializer.data)

    def put(self,request,pk):
        athlete=self.get_object(pk)
        serializer=AthleteSerializer(athlete,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        athlete=self.get_object(pk)
        athlete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#-----------
#-----------
# Create your views here.
@csrf_exempt
def index(request):
    return render(request,'index.html',context=None)

@csrf_exempt
def one2one(request):
    return render(request,'one2one.html',context=None)

@csrf_exempt
def one2oneinsertoptions(request):
    flag=0
    error=''
    rmp=''
    if request.method=='POST':
        rmp='True'
        carName=request.POST['car_name']
        carNumber=request.POST['car_number']
        fullName=request.POST['full_name']
        adhaarNumber=request.POST['adhaar_number']
        for row in Car.objects.all():
            if row.car_number==carNumber:
                error="this car number is already registered"
                flag=1
                break
        if(flag==0):
            p=Person(full_name=fullName,adhaar=adhaarNumber)
            p.save()
            c=Car(car_name=carName,car_number=carNumber,Owner=p)
            c.save()
            error='person registered'

    car_list=Car.objects.all()

    return render(request,'one2oneinsertoptions.html',{'status':rmp,'message':error})

@csrf_exempt
def one2oneextractoptions(request):
    car_list=Car.objects.all()
    person_list=Person.objects.all()
    print(car_list)
    print(person_list)
    # import pdb;
    # pdb.set_trace()
    return render(request,'one2oneextractoptions.html',{'success':car_list,'content':person_list})

@csrf_exempt
def one2many(request):
    return render(request,'one2many.html',context=None)

@csrf_exempt
def one2manyinsertoptions(request):
    flag=0
    if request.method=='POST':
        departmentID=request.POST['department_id']
        departmentName=request.POST['department_name']
        Budget=request.POST['budget']
        studentName=request.POST['student_name']
        Age=request.POST['age']
        Address=request.POST['address']
        rollNumber=request.POST['roll_number']
        for row in Student.objects.all():
            if row.roll_number==rollNumber:
                error="this roll number is already registered"
                flag=1
                break
        if(flag==0):
            d=Department(department_id=departmentID,department_name=departmentName,budget=Budget)
            d.save()
            s=Student(student_name=studentName,age=Age,address=Address,roll_number=rollNumber,allocated_department=d)
            s.save()

    return render(request,'one2manyinsertoptions.html',context=None)

@csrf_exempt
def one2manyextractoptions(request):
    student_list=Student.objects.all()
    department_list=Department.objects.all()
    print(student_list)
    print(department_list)
    # import pdb;
    # pdb.set_trace()
    return render(request,'one2manyextractoptions.html',{'success':student_list,'content':department_list})



@csrf_exempt
def many2many(request):
    return render(request,'many2many.html',context=None)

@csrf_exempt
def requestNresponse(request):
    if request.method=='POST':
        print("hello")
        var=request.POST['name']
        print(var)
        g=Game.objects.get(id=var)
        print(g)
        g.delete()
    g=Game.objects.all()
    return render(request,'requestNresponse.html',{'context':g})


@csrf_exempt
def athletescript(request):#athlete through javascript
    a=Athlete.objects.all()
    athlete_list=[]
    game_list=[]
    print(a)
    for i in a:
        print(i.id)
        game_str=''
        athlete=Athlete.objects.get(id=i.id)
        athlete_str=str(athlete)
        print(athlete)
        for j in athlete.games.all():
            game_str=game_str+str(j)+','
        print(game_str)
        athlete_str=""+athlete_str+"-> "+game_str
        athlete_list.append(athlete)
        game_list.append(athlete_str)
    print(athlete_list)
    print(game_list)
    return render(request,'athletescript.html',{'success':game_list})



@csrf_exempt
def many2manyinsertoptions(request):
    flag=0
    if request.method=='POST':
        gameName=request.POST['name']
        numberOfPlayers=request.POST['player_number']
        athleteName=request.POST['athlete_name']
        Age=request.POST['age']
        for row in Athlete.objects.all():
            if row.athlete_name==athleteName:
                error="this person is already registered with a game"
                flag=1

        if(flag==0):
            g1=Game(name=gameName,number_of_players=numberOfPlayers)
            g1.save()
            g2=Game(name='football',number_of_players=14)
            g2.save()
            a=Athlete(athlete_name=athleteName,age=Age)
            a.save()
            a.games.add(g1)
            a.games.add(g2)
            a.save()

    return render(request,'many2manyinsertoptions.html',context=None)


@csrf_exempt
def many2manyextractoptions(request):
    athlete_list=Athlete.objects.all()
    game_list=Game.objects.all()
    print(athlete_list)
    print(game_list)
    # import pdb;
    # pdb.set_trace()
    return render(request,'many2manyextractoptions.html',{'success':athlete_list,'content':game_list})

@csrf_exempt
def newathlete(request):
    flag=0
    pop=''
    if request.method=='POST':
        flag=1
        athleteName=request.POST['athlete_name']
        gameInterested=request.POST.getlist('sport')
        print(gameInterested)
        age=request.POST['age']
        a=Athlete(athlete_name=athleteName,age=age)
        a.save()
        for i in gameInterested:
            #print(i)
            i=i[:i.index("/")]
            i=int(i)
            game=Game.objects.get(id=i)
            a.games.add(game)
            a.save()
    if(flag==1):
        pop='student registered'
    game_list=Game.objects.all()
    return render(request,'newathlete.html',{'success':game_list,'message':pop})

@csrf_exempt
def newgame(request):
    if request.method=='POST':
        gameName=request.POST['name']
        numberOfPlayers=request.POST['number_of_players']
        g=Game(name=gameName,number_of_players=numberOfPlayers)
        g.save()
    game=Game.objects.all()
    return render(request,'newgame.html',{'context':game})

@csrf_exempt
def viewathlete(request):
    if request.method=="POST":
        searchResult=request.POST.get("search")
        print(searchResult)
        a=Athlete.objects.all()
        g=Game.objects.all()
        game_list=[]
        game_str=''
        for i in a:
            if str(i).find(searchResult)==0:
                print(True)
                athlete=Athlete.objects.get(athlete_name__startswith=searchResult)
                game_str=''
                athlete_str=str(athlete)
                print(athlete)
                for j in athlete.games.all():
                    game_str=game_str+str(j)+','
                print(game_str)
                athlete_str=""+athlete_str+"->"+game_str
                game_list.append(athlete_str)
        for i in g:
            if str(i).find(searchResult)==0:
                athleteForGame_str=''
                game=Game.objects.get(name__startswith=searchResult)
                for athlete in game.athlete_set.all():
                    game_str=''
                    athlete_str=str(athlete)
                    print(athlete)
                    for j in athlete.games.all():
                        game_str=game_str+str(j)+','
                    print(game_str)
                    athlete_str=""+athlete_str+"->"+game_str
                    game_list.append(athlete_str)

                # gameSelected_str=str(game)
                # print(game)
                # for j in game.athlete_set.all():
                #     athleteForGame_str=athleteForGame_str+str(j)+','
                # print(athleteForGame_str)
                # gameSelected_str=""+gameSelected_str+'->'+athleteForGame_str
                # game_list.append(gameSelected_str)

    else:
        a=Athlete.objects.all()
        athlete_list=[]
        game_list=[]
        print(a)
        for i in a:
            print(i.id)
            game_str=''
            athlete=Athlete.objects.get(id=i.id)
            athlete_str=str(athlete)
            print(athlete)
            for j in athlete.games.all():
                game_str=game_str+str(j)+','
            print(game_str)
            athlete_str=""+athlete_str+"-> "+game_str
            athlete_list.append(athlete)
            game_list.append(athlete_str)
        print(athlete_list)
        print(game_list)
    return render(request,'viewathlete.html',{'success':game_list})

@csrf_exempt
def viewgame(request):
    g=Game.objects.all()
    return render(request,'viewgame.html',{'context':g})

@csrf_exempt
def thisgameathlete(request):
    if request.method=='POST':
        gameSelected=request.POST.getlist('game')
        gameSelected=str(gameSelected)
        gameSelected=gameSelected[gameSelected.index("u")+2:gameSelected.index("/")]
        print(gameSelected)
        g=Game.objects.get(name=gameSelected)
        print(g)
        a=g.athlete_set.all()
        print(a)
    return render(request,'thisgameathlete.html',{'context':a})

@csrf_exempt
def editgame(request):
    if request.method=='POST':
        gameSelected=request.POST.getlist('sport')
        for i in gameSelected:
            i=i[:i.index("/")]
            i=int(i)
            game=Game.objects.get(id=i)
            game.delete()

    game=Game.objects.all()
    return render(request,'editgame.html',{'context':game})

@csrf_exempt
def editathlete(request):
    if request.method=='POST':
        athleteSelected=request.POST.getlist('player')
        for i in athleteSelected:
            i=i[:i.index("/")]
            i=int(i)
            athlete=Athlete.objects.get(id=i)
            athlete.delete()

    athlete=Athlete.objects.all()
    return render(request,'editathlete.html',{'context':athlete})

@csrf_exempt
def viewgamelist(request):
    g=Game.objects.all()
    return render(request,'viewgamelist.html',{'context':g})


@csrf_exempt
def deletegame(request,ID):
    if ID:
        print(ID)
        game=Game.objects.get(id=ID)
        game.delete()
    g=Game.objects.all()
    return HttpResponseRedirect("/viewgamelist/")



@csrf_exempt
def editgamelist(request):
    g=Game.objects.all()
    return render(request,'editgamelist.html',{'context':g})

@csrf_exempt
def editthatgame(request):
    if request.method=='POST':
        gameId=request.POST['sport']
        print(gameId)
        game=Game.objects.get(id=gameId)
        print(game)
        context={'id':game.id,'name':game.name,'no_of_players':game.number_of_players}
        # newName=request.POST['name']
        # newNumberOfPlayers=request.POST['number_of_players']
        # print(newName)
        # print(newNumberOfPlayers)

    return render(request,'editthatgame.html',context)

@csrf_exempt
def changegamedetail(request):
    if request.method=='POST':
        gameId=request.POST['game_id']
        print(gameId)
        game=Game.objects.get(id=gameId)
        newName=request.POST['name']
        newNumberOfPlayers=request.POST['number_of_players']
        print(newName)
        print(newNumberOfPlayers)
        game.name=newName
        game.number_of_players=newNumberOfPlayers
        game.save()

    g=Game.objects.all()
    return render(request,'changegamedetail.html',{'context':g})


@csrf_exempt
def editathletelist(request):
    a=Athlete.objects.all()
    return render(request,'editathletelist.html',{'context':a})



@csrf_exempt
def editthatathlete(request):
    if request.method=='POST':
        athleteId=request.POST['player']
        print(athleteId)
        athlete=Athlete.objects.get(id=athleteId)
        print(athlete)
        game=athlete.games.all()
        print(game)
        g=Game.objects.all()
        context={'id':athlete.id,'name':athlete.athlete_name,'age':athlete.age,'game_list':game,'full_game_list':g}
    return render(request,'editthatathlete.html',context)


@csrf_exempt
def changeathletedetail(request):
    if request.method=='POST':
        athleteId=request.POST['athlete_id']
        print(athleteId)
        athlete=Athlete.objects.get(id=athleteId)
        newName=request.POST['athlete_name']
        newAge=request.POST['age']
        print(newName)
        print(newAge)
        athlete.athlete_name=newName
        athlete.age=newAge
        athlete.save()
        athlete.games.clear()
        newGames=request.POST.getlist("sport")
        print(newGames)
        for i in newGames:
            i=str(i)
            i=int(i)
            game=Game.objects.get(id=i)
            athlete.games.add(game)
            athlete.save()
        context={'name':athlete.athlete_name,'age':athlete.age,'games':athlete.games.all()}

    return render(request,'changeathletedetail.html',context)

@csrf_exempt
def editgamebyurl(request,ID):
    print(request)
    print(ID)
    # gameId=request.GET.get('id', '')
    # print(gameId)
    # gameId=int(gameId)
    game=Game.objects.get(id=ID)
    print(game)
    context={'id':game.id,'name':game.name,'no_of_players':game.number_of_players}
    # newName=request.POST['name']
    # newNumberOfPlayers=request.POST['number_of_players']
    # print(newName)
    # print(newNumberOfPlayers)

    return render(request,'editthatgame.html',context)
