import os

srcdir = '.'
blddir = 'build'
VERSION = '0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  conf.env.append_value('CCFLAGS', ['-O3'])
  conf.env.append_value('CXXFLAGS', ['-O3'])
  conf.env.append_value("CPPPATH_PROTOBUF", "%s/include"%(os.environ['PROTOBUF']))
  conf.env.append_value("LIBPATH_PROTOBUF", "%s/lib"%(os.environ['PROTOBUF']))
  conf.env.append_value("LIB_PROTOBUF", "protobuf")


def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'protobuf_for_node'
  obj.source = 'protobuf_for_node.cc'
  obj.uselib = 'PROTOBUF'