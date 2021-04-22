import json
import  cloudscraper
import os.path
from os import path
import discord
from pip._vendor import requests
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import time
import asyncio
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as us
import os
from dotenv import load_dotenv
import win32com.client
import pythoncom
from pynotifier import Notification
import datetime
import re
x = datetime.datetime.now()
global this_day
this_day=x.strftime("%d")

#C:\Users\DELL\AppData\Local\Programs\Python\Python39\Scripts\pyinstaller 
load_dotenv()
global key
print('**************************************************')
print('*          BIENVENIDO BOT INNVICTUS              *')
print('*           -----yesa22 X_X-----                 *')
print('**************************************************')
print('Gracias por descargarme!')
print('Recuerda volver a cargar el bot cuando modifiques tus datos')
print('El bot esta trabajando por favor no cierres el programa...')
def getUrlAct():
    if path.exists("UrlActual.json"):
        if os.stat('UrlActual'+'.json').st_size!=0:
            with open('UrlActual'+'.json','r+') as json_file:
                url=json.load(json_file)
                print(url)
                return url
        else:
            print('Usa el comando watch para guardar una url')
            return False
    else:
        print('(UrlActual.json no existe)Usa el comando watch para guardar una url')
        return False
                 
def Webdriver(url,talla):
    driver=us.Chrome(executable_path=os.path.dirname(__file__)+'chromedriver.exe')
    driver.get(url)
    driver.find_element_by_xpath('//ul[@class="product-size__list"]/li[@class="product-size__option-wrapper"]/a[text()='+talla+']').click()
    element1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="notPreorderInfoSection"]/a[@onclick="ACC.productDetail.personalize.setConfirmationMsgAndSubmit(false)"]')))
    element1.click()
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="cart-button-margin hidden-xs hidden-sm"]/button')))
    driver.execute_script("arguments[0].click();", element)
    email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'j_username')))
    email.send_keys(os.getenv('EMAIL'))
    password= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'j_password')))
    password.send_keys(os.getenv('PASSWORD'))
    buttonIng = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="buttons"]/button')))
    driver.execute_script("arguments[0].click();", buttonIng)
    name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_firstName_0')))
    name.send_keys(os.getenv('NOMBRE'))
    lastName = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_lastName_0')))
    lastName.send_keys(os.getenv('APELLIDO'))
    aliasDir = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_displayName_0')))
    aliasDir.send_keys(os.getenv('ALIASDIR'))
    aliasDir = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_phone_0')))
    aliasDir.send_keys(os.getenv('TEL'))
    calle = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_line1_0')))
    calle.send_keys(os.getenv('CALLE'))
    numExt = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_numExterno_0')))
    numExt.send_keys(os.getenv('NUM_EXT'))
    numInt= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_numInterno_0')))
    numInt.send_keys(os.getenv('NUM_INT'))
    numInt= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_entrecalles_0')))
    numInt.send_keys(os.getenv('ENTRE_CALLES'))
    colonia = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_colonia_0')))
    colonia.send_keys(os.getenv('COLONIA'))
    numInt = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '_postcode_0')))
    numInt.send_keys(os.getenv('CODIGO_POSTAL'))
    selectRegion = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//select[@id='_regionIso_0']/option[text()='México']")))
    selectRegion.click()
    time.sleep(1)
    buttonGoEnvio = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@id="addressSubmit"]')))
    driver.execute_script("arguments[0].click();", buttonGoEnvio)
    buttonGoPago = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@id="deliveryMethodSubmit"]')))
    driver.execute_script("arguments[0].click();", buttonGoPago)
    checkTarj = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@id="payment_method_adyen"]')))
    driver.execute_script("arguments[0].click();", checkTarj)
    nomTitular = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Nombre"]')))
    nomTitular.send_keys(os.getenv('NOMBRE_TITULAR'))
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//span[@data-cse='encryptedCardNumber']/iframe[@class='js-iframe']")))
    nomTarj=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="1111 2222 3333 4444"]')))
    nomTarj.send_keys(os.getenv('NUM_TARJETA'))
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//span[@data-cse='encryptedSecurityCode']/iframe[@class='js-iframe']")))
    cvc=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="123"]')))
    cvc.send_keys(os.getenv('CVC'))
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//span[@data-cse='encryptedExpiryDate']/iframe[@class='js-iframe']")))
    dateMonth=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="MM/YY"]')))
    dateMonth.send_keys(os.getenv('FECHA_EXP'))
    driver.switch_to.default_content()
    buttonGoVerif = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@id="continueButton"]')))
    driver.execute_script("arguments[0].click();", buttonGoVerif)
    buttonEnd = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@id="placeOrder"]')))
    driver.execute_script("arguments[0].click();", buttonEnd)
    print('El proceso de compra se completo')
    
urlIndex='https://www.innvictus.com'

def SendEmbed(item):
    embed=discord.Embed(title=item.title)
    embed.set_author(name=urlIndex,icon_url=item.image)
    if (item.tallas):
        for talla in item.tallas:
            embed.add_field(name='Talla: ',value=talla)
    else:
        embed.add_field(name='No se encontraron tallas')
    if (item.models):
        for i,model in enumerate(item.models):
            embed.add_field(name='Modelo#'+str(i),value='[Ver]('+model+')')
    else:
        embed.add_field(name='No se encontraron modelos')
    embed.set_footer(text=item.price,icon_url=item.thumbnail)
    embed.set_thumbnail(url=item.thumbnail)
    embed.set_image(url=item.image)
    return embed


def search(list,item):
    for bd in list:
        if bd['code'] == item:
            return True
    return False
def searchModel(list,item):
    for bd in list:
        if bd == item:
            return True
    return False


def writeToJSONFIle(path, fileName, data):
    filePathNameWExt='./'+path+'/'+fileName+'.json'
    with open(filePathNameWExt,'w') as fp:
        json.dump(data, fp)



def cloudflare_get(url):
    retry = 6
    while retry > 0:
        try:
            res = cloudscraper.create_scraper().get(url)
            return res.text
        except Exception as e:
                print('Se encontro un capcha de seguridad espere un momento Jackiando la NASA xD...')
                retry = retry - 1
                time.sleep(5)

#getMeta
def get_metadata(url):
    tenis=type('',(),{})()
    r=cloudflare_get(url)
    soup=BeautifulSoup(r,'lxml')
    title=soup.find(class_="product-titles__name")
    if title is not None:
        tenis.found=True
        tenis.title=title.text
        price=soup.find(id="pdpCurrent_wholePart")
        photos=soup.find(class_="slider-main").find_all('img')
        models=soup.find_all(class_="product-colorways__item")
        sizes=soup.find_all(class_="product-size__option")
       
        if (len(photos)>0):
            tenis.image=urlIndex+photos[0].attrs['src']
            tenis.thumbnail=urlIndex+photos[1].attrs['src']
        else:
            tenis.image='https://static.thenounproject.com/png/140281-200.png'
    

        if (len(price)>0):
            tenis.price=price.text
        else:
            tenis.price='No se encontro precio'


        if (len(models)>0):
            tenis.models=list()
            for model in models:
                tenis.models.append(urlIndex+model.attrs['data-url'])


        else:
            tenis.models=False

        
        if (len(sizes)>0):
            tenis.tallas=list()
            for size in sizes:
                if not ('product-size__option--no-stock' in size.attrs['class']):
                    tenis.tallas.append(size.text)
        else:
            tenis.tallas=False
    else:
        tenis.found=False
    return tenis

def get_models(url):
    Getmodels=type('',(),{})()
    r=cloudflare_get(url)
    soup=BeautifulSoup(r,'lxml')
    title=soup.find(class_="product-titles__name")
    if title is not None:
        if os.path.isfile('UrlActual' +'.json'):
            os.remove('UrlActual'+'.json')
            writeToJSONFIle('./', 'UrlActual', url)
        else:
            writeToJSONFIle('./', 'UrlActual', url)
        Getmodels.found=True
        Getmodels.metadata=get_metadata(url)
        models=soup.find_all(class_="product-colorways__item")
        if (len(models)>0):
            Getmodels.models=list()
            Getmodels.Newmodels=list()
            for model in models:
                Getmodels.models.append(urlIndex+model.attrs['data-url'])
            if os.path.isfile('bdproduct' +'.json'):
                if os.stat('bdproduct'+'.json').st_size!=0:
                    with open('bdproduct'+'.json','r+') as json_file:
                        bd=json.load(json_file)
                    for i,itemModel in enumerate(Getmodels.models):
                        if(searchModel(bd,itemModel)==False):
                            Getmodels.Newmodels.append(itemModel)
                            bd.append(itemModel)
                    os.remove('bdproduct'+'.json')
                    writeToJSONFIle('./', 'bdproduct', bd)
                else:
                    os.remove('bdproduct'+'.json')
                    writeToJSONFIle('./', 'bdproduct', Getmodels.models)
                    Getmodels.Newmodels=Getmodels.models
            else:
                writeToJSONFIle('./','bdproduct',Getmodels.models)
                Getmodels.Newmodels=Getmodels.models

        else:
            Getmodels.models=False
    else:
        print('no encontro el titulo')
        Getmodels.found=False
    return Getmodels
    
def get_Key():
    r=cloudflare_get('https://yonline.tech')
    soup=BeautifulSoup(r,'lxml')
    if soup.find("div", {"id": "36n9cNR>rF.t-7/@"}) is not None:
        return True
    else: 
        return False

# desktop = os.path.join(os.getenv('programdata'),"Microsoft","Windows","Start Menu","Programs","StartUp") # path to where you want to put the .lnk
# path = os.path.join(os.path.abspath("."), "bot.lnk")
# target = os.path.join(os.path.abspath("."),"bot.exe")
# shell = win32com.client.Dispatch("WScript.Shell")
# shortcut = shell.CreateShortCut(path)
# shortcut.Targetpath = target
# shortcut.WindowStyle = 7 
# shortcut.save()
# print(os.path.abspath("."))
# print('se instalo')

bot= commands.Bot(command_prefix='>', description="Helper bot")



@bot.command()
async def ping(ctx):
    if get_Key() :
        await ctx.send('pong')
    else:
        await ctx.send('bot inactivo')

@bot.command()
async def watch(ctx,tiempo: int, url: str):
    if get_Key() :
        global bot_loop
        @tasks.loop(seconds=tiempo)
        async def bot_loop(ctx,url):
            print('Buscando..')
            Getmodels=get_models(url)
            if(Getmodels.found):
                await ctx.send(embed=SendEmbed(Getmodels.metadata))
                if(len(Getmodels.Newmodels)>0):
                    for urlItem in Getmodels.Newmodels:
                        tenis=get_metadata(urlItem)
                        if(tenis.found):
                            await ctx.send(embed=SendEmbed(tenis))
                        else:
                            print('No hay mas datos en esta url') 
                else:
                    print('El producto se encontro pero no se encontraron nuevos modelos') 
            else:
                print('No hay datos en esta url o el producto no se ha lanzado')
        bot_loop.start(ctx,url)
    else:
        await ctx.send('bot inactivo')
@bot.command()
async def stop(ctx):
    bot_loop.cancel()
    await ctx.send('Se detuvo la busqueda...')

@bot.command()
async def buy(ctx,talla):
    if get_Key():
        await ctx.send('Abriendo Chrome...')
        url=getUrlAct()
        if url:
            Webdriver(getUrlAct(),talla)
    else:
        await ctx.send('bot inactivo')
   
    
# @bot.command()
# async def install(ctx):   
#     desktop = os.path.join(os.getenv('programdata'),"Microsoft","Windows","Start Menu","Programs","StartUp") # path to where you want to put the .lnk
#     path = os.path.join(desktop, "botInvictus.lnk")
#     target = os.path.join(os.path.abspath("."),"bot.exe")
#     shell = win32com.client.Dispatch("WScript.Shell")
#     shortcut = shell.CreateShortCut(path)
#     shortcut.Targetpath = target
#     shortcut.WindowStyle = 7 
#     shortcut.save()
#     await ctx.send('Se instalo correctamente')


@bot.event
async def on_ready():
    if get_Key() :
        Notification(
            title='Bot Innvictus',
            description='El bot se ha iniciado',
            icon_path=os.path.dirname(__file__)+'favicon.ico', # On Windows .ico is required, on Linux - .png
            duration=5,                              # Duration in seconds
        ).send()
    else:
        await ctx.send('bot inactivo')
        Notification(
            title='Bot Innvictus',
            description='El bot esta inactivo',
            icon_path=os.path.dirname(__file__)+'favicon.ico', # On Windows .ico is required, on Linux - .png
            duration=5,                              # Duration in seconds
        ).send()
    
bot.run(os.getenv('BOT'))
