from typing import Any
from django.shortcuts import render
from django.views.generic import View
from django import forms

# form for regstraton

class RegistrationForm(forms.Form):
    name=forms.CharField(label="first name",max_length=23)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    phonenumbr=forms.CharField()
    username=forms.CharField()
    address=forms.CharField()
    def clean(self):
        self.cleaned_data=super().clean()
        phonenumbr=self.cleaned_data.get("phonenumbr")
        if len(phonenumbr)!=10:
            msg="invald phonenumbr"
            self.add_error("phonenumbr",msg)
# view for registration
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form}) 
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))
            return render(request,"login.html",{"form":form})
        else:
            print("error")
            return render(request,"signup.html",{"form":form})

           








# contact form
class ContactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField()
    sender=forms.EmailField()
# View for contact form

class ContactView(View):
    def get(self,request,*args,**kwargs):
        form=ContactForm()
        return render(request,"contact.html",{"form":form})
    








# bmi form creation 
class BmiForm(forms.Form):
    height_cm=forms.IntegerField(label="enter hieght in cm")
    wieght_kg=forms.IntegerField(label="enter weight in kg")

    def clean(self):
        self.cleaned_data=super().clean()
        wieght_kg=self.cleaned_data.get("wieght_kg")
        height_cm=self.cleaned_data.get("height_cm")
        # print(self.cleaned_data)
        if wieght_kg>800:
            msg="invalid wieght"
            self.add_error("wieght_kg",msg)
        if height_cm>200:
            msg="invalid hieght"
            self.add_error("height_cm",msg)

# view for bmi
class BmiView(View):
    def get(self,request,*args,**kwargs):
        form=BmiForm()
        return render(request,"bmi.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=BmiForm(request.POST)
        if form.is_valid():
            w_kg=form.cleaned_data.get("wieght_kg")
            h_cm=form.cleaned_data.get("height_cm")
            H_m=h_cm/100
            bmi=w_kg/(H_m**2)
            return render(request,"bmi.html",{"result":bmi,"form":form})
        else:
            return render(request,"bmi.html",{"form":form})
        


        # salary form
class SalaryForm(forms.Form):
    basic=forms.IntegerField()
    hra=forms.IntegerField()
    speclallowance=forms.IntegerField()
    ta=forms.IntegerField()
    pf=forms.IntegerField()

    def clean(self):
        self.cleaned_data=super().clean()
        basic=self.cleaned_data.get("basic")
        # hra=self.cleaned_data.get("hra")
        # speclallowance=self.cleaned_data.get("speclallowance")
        # ta=self.cleaned_data.get("ta")
        # pf=self.cleaned_data.get("pf")
        if(basic<0):
            msg="invalid basic salary"
            self.add_error("basic",msg)

class SalaryView(View):
    def get(self,request,*args,**kwargs):
        form=SalaryForm()
        return render(request,"salary.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=SalaryForm(request.POST)
        if form.is_valid():
            basic_salary=form.cleaned_data.get("basic")
            hra_=form.cleaned_data.get("hra")
            sa=form.cleaned_data.get("speclallowance")
            ta=form.cleaned_data.get("ta")
            pf=form.cleaned_data.get("pf")
            net_salary=(basic_salary+hra_+sa+ta-pf)
            return render(request,"salary.html",{"form":form,"result":net_salary})
        else:
            return render(request,"salary.html",{"form":form})








# Create your views here.
class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        print("printing helloworld inside server")
        return render(request,"helloworld.html")
    
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"goodmorning.html")
class GoodAfterNoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"goodafternoon.html")
    






class calculatorForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()
    def clean(self):
        self.cleaned_data=super().clean()
        num1=self.cleaned_data.get("num1")
        num2=self.cleaned_data.get("num2")
        if num1==0:
            msg="invalid num"
            self.add_error("num1",msg)
        if num2==0:
            msg="invalid num"
            self.add_error("num2",msg)

    


    # def clean(self):
    #     self.cleaned_data=super().clean()
    #     n1=self.cleaned_data.get("num1")
    #     n2=self.cleaned_data.get("num2")
    #     if n1<1:
    #         msg="pls provde a numbr greater than 0"
    #         self.add_error("num1",msg)
    #     if n2<1:
    #         msg="pls provde a numbr greater than 0"
    #         self.add_error("num2",msg)
        





class AdditionView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm()
        return render(request,"addition.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)+int(n2)
            print(form.cleaned_data)
            return render(request,"addition.html",{"result":res,"form":form})
        else:
            return render(request,"addition.html",{"form":form})
        






class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm()
        return render(request,"sub.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)-int(n2)
            return render(request,"sub.html",{"result":res,"form":form})
        else:
            return render(request,"sub.html",{"form":form})
        







    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm()
        return render(request,"multi.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)*int(n2)
            return render(request,"multi.html",{"result":res,"form":form})
        else:
            return render(request,"muti.html",{"form":form})
        







class CubeView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm()
        return render(request,"cube.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            res=int(n1)**3
            return render(request,"cube.html",{"result":res,"form":form})
        else:
            return render(request,"cube.html",{"form":form})
        





class DivisionView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm()
        return render(request,"div.html")
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n1=request.POST.get("num1")  
            n2=request.POST.get("num2")
            res=int(n1)/int(n2)
            return render(request,"div.html",{"result":res})
        else:
            return render(request,"cube.html",{"form":form})


class FactorialView(View):
    def get(self,request,*args,**kwargs):
        form=calculatorForm
        return render(request,"fac.html")
    def post(self,request,*args,**kwargs):
        form=calculatorForm(request.POST)
        if form.is_valid():
            n=int(form.cleaned_data.get("num1"))  
            fac=1
        for i in range(1,n+1):
            fac*=1
       
        return render(request,"div.html",{"result":fac})
    



    

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    






class OperationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"operation.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        requestdotPOST={"num1":100,"num2":200,"mul":""}
        if "add" in request.POST:
            res=n1+n2
        elif"sub" in request.POST:
            res=n1-n2
        elif"mul" in request.POST:
            res=n1*n2
        return render(request,"operation.html",{"result":res})
    











        
