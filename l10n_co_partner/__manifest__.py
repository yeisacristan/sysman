# -*- coding: utf-8 -*-
# Co-Author        Juan David Pelaez (Stefanini Sysman SAS), jdsoto1@sysman.com.co
#                  Jhair Alejandro Escobar (Stefanini Sysman SAS), e_japulido@sysman.com.co
#                  Jonathan David Medina Sanchez (Stefanini Sysman SAS), jdsanchez1@sysman.com.co
#                  Alejandro Olano ( Sysman SAS), jaramirez@sysman.com.co

{
    "name": "l10n_co_partner",
    "category": "Localization",
    "version": "15.0.3",
    "author": "Sysman SAS",
    "website": "http://www.sysman.com.co",
    "license": "OPL-1",
    "summary": "Ajustes Contactos Localización Colombia",
    "depends": ["account", "l10n_co"],
    "data": [
        "security/ir.model.access.csv",
        "security/res_partner_security.xml",
        "data/l10n_co_address_type.xml",
        "data/ciiu.value.csv",
        "data/ir_cron.xml",
        "views/ciiu_values_views.xml",
        "views/l10n_co_address_views.xml",
        "views/latam_identification_type_views.xml",
        "views/res_country_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "pre_init_hook": "l10n_co_partner_pre_init_hook",
}
