
![Image description](https://github.com/csfeeser/TLG-Python/blob/master/skill%20level.png?raw=true)

### MAKE YOUR WAY THROUGH AS MANY CHALLENGES AS YOU CAN:

0. Find your name in the data below. Write a script that prints your first name from the “JSON” data shown here.

0. Write a script that outputs **ONE** of the following (fill in the blank!):

	“My name is ______ and my spirit animal is _______.”

	“My name is ______ and my skills are _______.”

	“My name is ______ and my super power is _______.” 


0. Write a script that loops through the entire list. Have it output the following for every person in class:

#### EXAMPLE:
	
    Name: Askia Wingfield
	Skill Level: Astonishing
	Spirit Animal: Lion
	Super Power: Regenerative Healing Factor
		
	Name: Chen Xin
	Skill Level: Awe-inspiring
	Spirit Animal: Porcupine
	Super Power: Adoptive Muscle Memory

[...and so on!]

[Yikes! Is this hard to read? Click here for a pretty-print website you can copy-paste this into!](https://jsonformatter.org/json-pretty-print)

mess = {"all": [{"First":"Askia","Last":"Wingfield","Skill Level":"astonishing","Spirit Animal":"lion","Super Power":"Regenerative Healing Factor"},{"First":"Chen","Last":"Xin","Skill Level":"awe-inspiring","Spirit Animal":"porcupine","Super Power":"Adoptive Muscle Memory"},{"First":"Everett","Last":"Strunk","Skill Level":"breathtaking","Spirit Animal":"mandrill","Super Power":"Body Part Substitution"},{"First":"Jacob","Last":"Roe","Skill Level":"fearsome","Spirit Animal":"guinea pig","Super Power":"Anatomical Liberation"},{"First":"Josh","Last":"Ayala","Skill Level":"formidable","Spirit Animal":"camel","Super Power":"Additional Limbs"},{"First":"Kevin","Last":"Martinez","Skill Level":"imposing","Spirit Animal":"panther","Super Power":"Organic Constructs"},{"First":"Luke","Last":"Thompson","Skill Level":"impressive","Spirit Animal":"coati","Super Power":"Deflection"},{"First":"Marco","Last":"Santos","Skill Level":"magnificent","Spirit Animal":"bumblebee","Super Power":"Replication"},{"First":"Michael","Last":"Williams","Skill Level":"overwhelming","Spirit Animal":"fish","Super Power":"Invisibility"},{"First":"Mike","Last":"Wright","Skill Level":"stunning","Spirit Animal":"mink","Super Power":"Needle Projection"},{"First":"Oscar","Last":"Abalos","Skill Level":"wondrous","Spirit Animal":"ermine","Super Power":"Immobility"},{"First":"Ryan","Last":"Larson","Skill Level":"grand","Spirit Animal":"marmoset","Super Power":"Camouflage"},{"First":"Shirley","Last":"Wu","Skill Level":"mind-blowing","Spirit Animal":"koala","Super Power":"Self-Detonation"}]}

#### Challenge 1 Solution:

    print(mess['all'][7]['First'])

#### Challenge 1 Solution:

    print(f"My name is {mess['all'][7]['First']} {mess['all'][7]['Last']} and my spirit animal is a {mess['all'][7]['Spirit Animal']}")

#### Challenge 3 Solution SIMPLE:

    for x in mess["all"]:
        print(f"""
        Name: {x['First']} {x['Last']}
        Skill Level: {x['Skill Level']}
        Spirit Animal: {x['Spirit Animal']}
        Super Power: {x['Super Power']}""")

#### Challenge 3 Solution ADVANCED- thanks Chen Xin!

    len_list = len(challenge_list['all'])

    print(len_list)

    for i in range(0,len_list):
        first_name = challenge_list["all"][i]['First']
        last_name = challenge_list["all"][i]['Last']
        skill_level = challenge_list["all"][i]['Skill Level']
        spirit_animal = challenge_list["all"][i]['Spirit Animal']
        super_power = challenge_list["all"][i]['Super Power']
        print(f'''
        Name: {first_name} {last_name}
        Skill Level: {skill_level}
        Spirit Animal: {spirit_animal}
        Super Power: {super_power}
        ''')
        print("------------------------------------------")
