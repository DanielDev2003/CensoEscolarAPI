from helpers.application import app , api
from helpers.database import db
from helpers.CORS import cors

from models.Uf import Uf
from models.Mesorregiao import Mesorregiao
from models.Microrregiao import Microrregiao
from models.Municipio import Municipio
from models.Entidade import Entidade

from resources.IndexResource import IndexResource
#from resources.InstituicaoResource import InstituicoesResource, InstituicaoResource, InstituicoesConsultaResource, InstituicoesConsultaPorAnoResource,InstituicoesPorCidadeResource
from resources.UfResource import UfResource
from resources.EntidadeResource import EntidadeResource, EntidadeConsultaAnoResource, EntidadeConsultaMatriculaEstadoResource, EntidadePConsultaMatriculaCidadeResource
from resources.MesorregiaoResource import MesorregiaoResource
from resources.MicrorregiaoResource import MicrorregiaoResource
from resources.MunicipioResource import MunicipioResource
cors.init_app(app)

api.add_resource(IndexResource, '/')

#api.add_resource(InstituicoesResource, '/instituicoes')
#api.add_resource(InstituicaoResource, '/instituicoes/<int:id>')
#api.add_resource(InstituicoesConsultaResource, '/instituicoes/anos')
#api.add_resource(InstituicoesConsultaPorAnoResource, '/instituicoes_consulta')
#api.add_resource(InstituicoesPorCidadeResource, '/instituicoes_cidades')

#EndPoint Entidade(Instituicao)
api.add_resource(EntidadeResource, '/instituicoes')
api.add_resource(EntidadeConsultaAnoResource, '/instituicoes/anos')
api.add_resource(EntidadeConsultaMatriculaEstadoResource, '/instituicoes/matriculas_estado' )
api.add_resource(EntidadePConsultaMatriculaCidadeResource, '/instituicoes/matriculas_cidade')

#EndPoint UF
api.add_resource(UfResource,'/ufs')

#EndPoint Mesorregião
api.add_resource(MesorregiaoResource, '/instituicoes/mesorregiao')

#EndPoint Microrregião
api.add_resource(MicrorregiaoResource, '/instituicoes/microrregiao')

#EndPoint Municipio
api.add_resource(MunicipioResource, '/instituicoes/municipio')

with app.app_context():
    db.create_all()


 






    