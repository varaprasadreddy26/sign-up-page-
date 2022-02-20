from fastapi import FastAPI ,Depends
import schemas, models
from database import  engine ,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
@app.post('/blog')
def create (request:schemas.Blog, db: Session = Depends(get_db)):
    new_Blog = models.Blog(name=request.name, email=request.email, password=request.password)
    db.add(new_Blog)
    db.commit()
    db.refresh(new_Blog)
    return new_Blog
  

    