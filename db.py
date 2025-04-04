from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base  # Updated import

# Modern declarative base (SQLAlchemy 2.0+)
Base = declarative_base()


class Document(Base):
    _tablename_ = 'documents'

    id = Column(Integer, primary_key=True)
    filename = Column(String(100))
    content = Column(Text)
    filetype = Column(String(10))
    filepath = Column(String(255))  # Added for better tracking


class Database:
    def _init_(self, db_url='sqlite:///documents.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_document(self, filename, content, filetype, filepath):
        session = self.Session()
        try:
            doc = Document(
                filename=filename,
                content=content,
                filetype=filetype,
                filepath=filepath
            )
            session.add(doc)
            session.commit()
            return doc.id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def search(self, keyword):
        session = self.Session()
        try:
            from sqlalchemy import or_
            results = session.query(Document).filter(
                or_(
                    Document.content.ilike(f"%{keyword}%"),
                    Document.filename.ilike(f"%{keyword}%")
                )
            ).all()
            return results
        finally:
            session.close()

    def get_all_documents(self):
        session = self.Session()
        try:
            return session.query(Document).all()
        finally:
            session.close()