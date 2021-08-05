from ..base._loaders import Loaders
from ..processor.loader import *
from ..recursive.loader import *
from ._modelInfoLoader import ModelInfoLoader


class DefaultLoaders(Loaders):

  def __init__(self):
    super().__init__()
    self.addLoader(Slice1DProcessorLoader())
    self.addLoader(ContextProcessorLoader())
    self.addLoader(AutoPadding1DProcessorLoader())
    self.addLoader(Erased1DProcessorLoader())
    self.addLoader(NoneProcessorLoader())
    self.addLoader(SparseProcessorLoader())
    self.addLoader(CustomRecursiveLoader())
    self.addLoader(SparseRecursiveLoader())
    self.addLoader(ModelInfoLoader())
