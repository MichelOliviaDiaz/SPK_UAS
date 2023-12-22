from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Laptop(Base):
    __tablename__ = "laptop"

    id : Mapped[int] = mapped_column(primary_key=True)
    nama_produk : Mapped[str]
    harga_per_unit : Mapped[str]
    processor : Mapped[str]
    ram : Mapped[str]
    ukuran_layar : Mapped[str]
    storage : Mapped[str]

    def __repr__(self) -> str :
        return f"id={self.id}, nama_produk={self.nama_produk}, harga_per_unit={self.harga_per_unit}, processor={self.processor}, ram={self.ram}, ukuran_layar={self.ukuran_layar}, storage={self.storage}"

