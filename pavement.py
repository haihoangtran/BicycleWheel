from paver.easy import *
import os
import glob

@task
def test():
  sh('nosetests code/test/*.py --with-coverage')
  #sh('nosetests code/test/*.py')
  pass

@task
def runui():
  sh('python code/src/ui/BicycleWheelGUI.py')
  pass
  
@task
def clean():
  os.remove('savedFile.txt')
  os.path.exists('.coverage') and os.remove('.coverage')
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  pass

@task
@needs(['test', 'runui', 'clean'])
def default():
  pass