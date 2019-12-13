artists = {    
    "국가": {
        "Korea": "Seoul",
        "Japan": "Tokyo"
    }
}    

# 한국의 수도는?
# 1번방법
print(artists["국가"]["Korea"])
# 2번 방법
print(artists.get("국가").get("Korea"))