from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from nva.folderbehaviors.interfaces import ISchmuckbilder
from plone.z3cform import layout
from z3c.form import form

class SchmuckbildPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = ISchmuckbilder

SchmuckbildControlPanelView = layout.wrap_form(SchmuckbildPanelForm, ControlPanelFormWrapper)
SchmuckbildControlPanelView.label = u"Nachrichten-Handhabung"
