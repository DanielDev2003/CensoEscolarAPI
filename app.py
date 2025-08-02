from helpers.application import app , api
#from helpers.database import db
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


cors.init_app(app)

api.add_resource(IndexResource, '/')

#api.add_resource(InstituicoesResource, '/instituicoes')
#api.add_resource(InstituicaoResource, '/instituicoes/<int:id>')
#api.add_resource(InstituicoesConsultaResource, '/instituicoes/anos')
#api.add_resource(InstituicoesConsultaPorAnoResource, '/instituicoes_consulta')
#api.add_resource(InstituicoesPorCidadeResource, '/instituicoes_cidades')

api.add_resource(EntidadeResource, '/instituicoes')
api.add_resource(EntidadeConsultaAnoResource, '/instituicoes/anos')
api.add_resource(EntidadeConsultaMatriculaEstadoResource, '/instituicoes/matriculas_estado' )
api.add_resource(EntidadePConsultaMatriculaCidadeResource, '/instituicoes/matriculas_cidade')

api.add_resource(UfResource,'/ufs')

# with app.app_context():
#     db.create_all()









    