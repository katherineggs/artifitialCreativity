import pandas as pd
import os

specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", "_", "=", "<", ">", "Œ", "€", "/"]
notLyrics = ["unreleased", "lyrics for this song have not yet been released please come back once they have been released",
"lyrics for this song have yet to be released please check back once the song has been released", "lyrics from snippet",
"lyrics will be available upon release stay tuned", "tba", "ariii  kim", "released in 09", "snippet", "come back soon when there is lyrics",
"no lyrics for this song come back soon"]

def readAllCSVs(folderP):
    artists = []
    lyrics = []

    for filename in os.listdir(folderP):
        file = pd.read_csv(folderP+filename)
        file = file.drop(["Artist", "Title", "Album", "Date", "Year"], axis=1) # intentar no botar todas
        # artists.append(filename.replace(".csv",""))
        for eachLyric in file["Lyric"]:
            for spec in specialChars:
                if spec in str(eachLyric):
                    eachLyric = eachLyric.replace(spec, "")
                    # print("yes")
            for noL in notLyrics:
                if str(eachLyric).startswith(noL):
                    print("x")
                    break

            artists.append(filename.replace(".csv",""))
            lyrics.append(eachLyric)
    
    df = pd.DataFrame(
    {'Artist': artists,
     'Lyrics': lyrics
    })
    
    return df
