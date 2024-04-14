# Ebtesam Aloubid - 101260655
a= input ("Chose a subgenres by typing it: 1. War 2.Fantasy. if you need help type the word(Hlep)").upper()
# if the user chose war use the fallowing code, if the user nneds help jump to line 36, or if the user chose fantasy jump to line 38
if a == "WAR" :
    # Questions for the war subgenres 
    print ("To start chose a movie title: 1.Hearts of the World (1918), 2.A Revival of War Films in the Mid-1920s 3.What Price Glory? (1926) 4.Wings (1927) 5.Hell’s Angels (1930) 6. All Quiet on the Western Front (1930) 7. Westfront 1918 (1930) 8.The Dawn Patrol (1930). 9.The Third Reich in The Great Dictator (1940).10. For Whom the Bell Tolls (1943)")

    if input("Did it include actual battle footage filmed on location in 1917 on the outskirts of the world war I war itself").upper() == "YES":
        print ("The movie title is Hearts of the World (1918)")
    else: 
        if input ("did it talk about a love story between a French peasant girl and a soldier during the World War I").upper() == "YES":
            # French peasant in common 
                if input ("Did it talk about the struggle for survival by three soldier-comrades in the trenches?").upper() == "YES": 
                 print ("The movie title is A Revival of War Films in the Mid-1920s")
                else:
                    print ("The movie title is What Price Glory? (1926)")
        else :
            if input("Was It the first and the only silent film to be awarded Best Picture").upper() == "YES" :
                print ("Wings (1927)")
            else: 
                if input("Did it talk about the story of love with two English brothers who were British Royal Flying Corps pilots.").upper() == "YES":
                    print ("The movie title is Hell’s Angels (1930)")
                else:
                    if input("Was it an anti war movie?").upper() =="YES":
                        # both are anti war movies 
                        if input("Was it based upon the novel by Erich Maria Remarque that viewed the Great War from the German point of view?").upper()=="YES":
                            print ("The movie title is All Quiet on the Western Front (1930)")
                        else:
                            print ("The movie title is  Westfront 1918 (1930)")
                    else :
                        if input("Did it talk about the story of the British Royal Flying Corps at a remote outpost in France during World War ").upper()=="YES":
                            print ("The movie title is The Dawn Patrol (1930) ")
                        else: 
                            if input (" Was it the director/actor's first all-talking picture by Charlie Chaplin lampooned Adolf Hitler.").upper()=="YES":
                                print ("The movie title is  The Third Reich in The Great Dictator (1940)")
                            else: 
                                print ("The movie title is For Whom the Bell Tolls (1943)")
             
if a == "HELP":
        print ("In the game first you are going to chose a subgenres. Then a list of 10 movies will show up, you are doing to chose a movie, them answer questions using yes or no to gues the movie name")
else:
    # questions for fantasy options 
     if a == "FANTASY":
        print ("Chose a movie: 1.  Voyage Dans La Lune  2. The Thief of Bagdad  3.The Wizard of Oz 4.Mighty Joe Young 5.When Worlds Collide 6.Destination Moon 7.The First Men in the Moon 8.Clash of the Titans 9.The Dark Crystal 10.Labyrinth")
       # movie list 
        if input("Was it a silent fantasy film about a trip to the Moon").upper()=="YES":
            print ("The movir title is Voyage Dans La Lune")
        else:
            if input("Was it a children's fantasy/musical").upper() == "YES" :
                # both for kids 
                if input ("Was it masterfully retold in the Arabian Nights tale? ").upper() == "YES":
                    print ("The movie title is The Thief of Bagdad")
                else:
                    print ("The movie title is The Wizard of Oz ")
            else :
                if input ("Is it an animation by George Pal? ").upper()== "YES" :
                    # both by George Pal
                    if input ("Did Goeorge Pal won Best Visual (Special) Effects Oscars for the exciting, low-budget sci-fi disaster film for this movie?").upper()=="YES":
                        print ("The movie title is When Worlds Collide")
                    else:
                        print ("Destination Moon")
                else:
                    if input ("Was it by Ray Harryhausen where it featured grotesque giant monsters, fabulous Greek mythological, or medieval Arabian figures? ").upper()=="YES":
                        print ("The movie title is Mighty Joe Young ")
                    else:
                        if input("Was it by Harryhausen films in the mid-60s").upper()=="YES":
                            # both by  Harryhausen
                            if input("Was it about a space trip to the lunar surface (with an alien civilization) ? ").upper() == "YES":
                                print ("The movie title is The First Men in the Moon")
                            else:
                                print ("Clash of the Titans")
                        else :
                           if input("Is it a delightful children's fantasy tale with Muppets? ").upper() == "YES" :
                               print ("The movie title is The Dark Crystal ")
                           else:
                            print ("The movie title is Labyrinth")

                    
                    