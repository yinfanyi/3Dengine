from vbo import *
from shader_program import ShaderProgram
import moderngl as mgl

class VAO:
    def __init__(self, ctx) -> None:
        self.ctx: mgl.Context = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
    
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube']
        )
        
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat']
        )
        
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox']
        )
        
    def get_vao(self, program: ShaderProgram, vbo:BaseVBO) -> mgl.VertexArray: 
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
        
        