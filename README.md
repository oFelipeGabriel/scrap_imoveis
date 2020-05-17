## Projeto para raspagem de dados públicos dos sites:

* [https://www.grupokaza.com.br/](https://www.grupokaza.com.br/)
* [https://www.imobiliariamaciel.com.br/](https://www.imobiliariamaciel.com.br/)
* [https://www.novafreitas.com.br/](https://www.novafreitas.com.br/)
* [http://www.geracaoimoveis.com.br/](http://www.geracaoimoveis.com.br/)
* [https://www.piramideimoveissjc.com.br/](https://www.piramideimoveissjc.com.br/)
* [https://www.lopes.com.br/](https://www.lopes.com.br/)
* [https://www.kogake.com.br/](https://www.kogake.com.br/)

```bash
git clone https://github.com/oFelipeGabriel/scrap_imoveis.git

virtualenv -m python3 env_scrap_imoveis

source env_scrap_imoveis/bin/activate

cd scrap_imoveis

pip install -r requirements.txt

python grupokaza.py
```

