# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define capo = Character("Capucinho Vermelho", color="#990000", voice_tag="audio/Capuchinho")#👧🟥
define lenhador = Character("Lenhador", color="#330000")#🪓
define mae = Character("Mãe", color="#ab17e7")
define avo = Character("Avozinha", color="#ffffff")#👵
define lobo = Character("Lobo Mau", color="#000000")#🐺

label start:
    play music nature
    scene casa mae
    with fade

## Introduçào
    "ERA UMA VEZ uma linda menina que vivia numa aldeia, a quem a sua avó lhe deu um capocho vermelho, e desde então passaram a chamar-lhe de Capuchinho Vermelho."

    show redhood
    with dissolve

    "Um dia a mãe chamou-a e pediu-lhe um favor:"
    show mother at right
    with dissolve

    voice mae1

    mae "Coloquei nesta cesta um bolo e uma garrafa de leite. Leva-o à avozinha, que tem andado adoentada. Vai agora de manhã antes que fique muito quente, e enquanto estiveres a caminho tem cuidado. Não corras, não saias do caminho e não fales com estranhos."

## Na floresta

    scene caminhos
    with fade
    voice queres_seguir_o_caminho
    menu:

            "Queres seguir o caminho?"

            "{image=images/cross.png}": 
                jump caminhoErrado
            "{image=images/check.png}":
                jump caminho
label caminhoErrado:
    "Ho não seguiste o caminho errado."
    return

label caminho:

    show floresta
    with dissolve
    show redhood
    with dissolve

    menu:
            "Queres correr?"

            "{image=images/check.png}":
                jump caiste
            "{image=images/cross.png}":
                jump naoCorreu

label caiste:
    "FINAL : Cai e as coisas partem-se"
    return

label naoCorreu:

## Falar com o LOBO

    "Ia a Capuchinho Vermelho pelo caminho quando, de repente, encontrou o Lobo. A Capuchinho não o conhecia, mas ele até parecia simpático e ela não tinha medo dele."

    show lobo at left
    with dissolve

    "Este, com uma voz muito doce disse-lhe:"

    menu:
        lobo "Bom dia Capuchinho Vermelho. Para onde vais tão cedo?"

        "{image=images/cross.png}":
            voice "audio/Capuchinho_2.mp3"
            capo "Bom dia Sr. Lobo, desculpe mas não falo com estranhos."
            jump segue2
        "{image=images/check.png}":
            voice "audio/Capuchinho_1.mp3"
            capo "Vou a casa da minha avó"

    menu:
        lobo "E o que tens nessa cesta?"
        "{image=images/check.png}":
            voice "audio/Capuchinho_3.mp3"
            capo "Um bolo e uma garrafa de leite. A minha avó está doente e quero dar-lhe algo doce para a tentar animar."
        "{image=images/cross.png}":
            voice "audio/Capuchinho_4.mp3"
            capo "Não tens nada a haver com isso."

    menu:
        lobo "Onde vive a tua avó, Capuchinho Vermelho?"
        "{image=images/cross.png}":
            voice  "audio/Capuchinho_2.mp3"
            capo "Não tens nada a haver com isso."
            jump segue
        "{image=images/check.png}":
            voice "audio/Capuchinho_5.mp3"
            capo "No lago depois da floresta. A casa dela fica debaixo de três grandes carvalhos e as castanheiras ficam bem abaixo."

    menu:
        lobo "Olha só, Capuchinho Vermelho, como são belas as flores por aqui. Porque não apanhas algumas para a tua avó? Isso provavelmente iria animá-la."
        "{image=images/check.png}":
            jump historiaOriginal
        "{image=images/cross.png}":
            jump ajuda

            ## SEGUE

label segue2:
    
    menu:
        lobo "E o que tens nessa cesta?"
        "{image=images/check.png}":
            voice "audio/Capuchinho_3.mp3"
            capo "Um bolo e uma garrafa de leite. A minha avó está doente e quero dar-lhe algo doce para a tentar animar."
        "{image=images/cross.png}":
            voice "audio/Capuchinho_4.mp3"
            capo "Não tens nada a haver com isso."
    
label segue:
    hide lobo
    menu:
        "Volta para trás?"
        "{image=images/check.png}":
            "FINAL:\
            Vai de tarde em vez de manhã."
            return
        "{image=images/cross.png}":
            jump ajuda
            
            
label ajuda:
    show lenhador at left
    with dissolve
    
    
    menu:
        "Então apareceu o Lenhador. A Capuchinho pensou se lhe devia pedir ajuda."
        "{image=images/cross.png}":
                hide lenhador
                jump comeduas
        "{image=images/check.png}":
                jump falarComLenhador


label falarComLenhador:
    "A Capuchinho foi esperta e andou no sentido do Caçador sem o Lobo perceber.
Quando o Caçador olhou para ela, fez-lhe sinal a pedir ajuda."
    "Então ele matou o Lobo e acompanhou a Capuchinho até casa da sua avó."
    scene casa avo
    with fade
    show redhood
    with dissolve
    show avo at left
    with dissolve
    show lenhador at right
    "Ela, a Avózinha e o Caçador comeram o bolo e beberam o leite, felizes por tudo ter acabado bem."
    return

label comeduas:
    "Final
    O lobo come as duas."
    return
