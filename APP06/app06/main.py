import flet as ft

#se importa la librería random 
import randon

def main(page: ft.page):
    
    global numero_secreto, entread_numero, text_resultado, boton_adivinar 
    
    page.titlt ="Adivina el número"
    
    
    numero_secreto=randon.randint(1,100)
    
    
    titulo=ft.Text("Adivina el numero", size=25, color="wrhite")
    entrada_numero=ft.TextField(label="Tu adivinanza entre 1 y 100",width=300)
    boton_adivnar=ft.ElevatedButton("Adivinar")
    text_resultado=ft.Text("",color="white")

        contenedor_principal=ft.Container(
            content=ft.Column(
                controlls =[
                    titulo,
                    entrada_numero,
                    boton_adivinar,
                    text_resultado,
                    ft.image(
                        src="https://i.ibb.co/Gxgryg9/laser.gif"
                        fit=ft.ImageFit.COVER,
                        width=350,
                        height=300
                    )
                ],aligment="CENTER"
                horizontal_aligment="CETER"
                spacing = 20 
        ),
        bgcolor="blue",
        widt=page,window.width, 
        height=page,window.width, 
        padding=20
        )
    page.add(contenedor_principal)
    
    
    
ft.app(main)
