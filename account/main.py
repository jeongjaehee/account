@app.post('/signup')
def signup(id:Annotated[str,Form()],password:Annotated[str,Form()]):
    print(id,password)
def signup(id:Annotated[str,Form()],
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    cur.execute(f"""
                INSERT INTO users(id,name,email,password)
                VALUES ('{id}','{name}','{email}','{password}')
                """)
    con.commit()
    return '200'
           
app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")