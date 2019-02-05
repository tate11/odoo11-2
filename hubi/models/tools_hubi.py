# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ..controllers import ctrl_print

@api.model
def _default_is_Visible_class(self, valeur): 
    retour = False
    option=self.env['hubi.module_option']

    check_opt=option.search([('name','=', valeur),('company_id','=', self.company_id.id)])
    for check in check_opt:
        retour = check.state
    return retour

@api.one    
def _is_Visible_class(self, origin):
    # Product
    if origin == 'Product':
            self.is_fonction_deporte = False
            self.is_etiquette = False
            self.is_etiq_marenne = False
            self.is_etiq_prod_edition = False
            self.is_etiq_prod_libelle = False
            self.is_etiq_prod_lib_espagnol = False
            self.is_etiq_prod_lib_latin = False 
        
    if origin == 'Product' or origin == 'PriceList' :   
            self.is_etiq_format = False
        
            self.is_tarif_option = False
            self.is_tarif_code_interne = False
            self.is_tarif_ref_client = False
            self.is_tarif_lib_promo = False     

    # Partner
    if origin == 'Partner' :
            self.is_frs = False
            self.is_edi_facture = False
            self.is_edi_transporteur = False
            self.is_bl_valorise = False
            self.is_etiq_lot_auto = False
            self.is_prix_kg = False
            self.is_type_tiers = False
            self.is_etiq_dlc = False
            self.is_etiq_couleur_client = False
            self.is_etiq_ean_128 = False
            ##self.is_etiq_mode = False
            self.is_etiq_type = False
            self.is_export_compta = False
            self.is_fonction_deporte = False
            self.is_regr_prod_fac = False                                                         
       

    if origin == 'Partner' or origin == 'PriceList' :
            self.is_ifls = False
       
    self.is_etiq_mode = False  
             
    option=self.env['hubi.module_option']
         
    check_opt=option.search([('name','=','ETIQ_MODE'),('company_id','=', self.company_id.id)])
    for check in check_opt:
        self.is_etiq_mode = check.state 

    # Product
    if origin == 'Product':
            check_opt=option.search([('name','=','FONCTION_DEPORTE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_fonction_deporte = check.state  
            check_opt=option.search([('name','=','ETIQUETTE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiquette = check.state 
            
            check_opt=option.search([('name','=','ETIQ_MARENNE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_marenne = check.state 
            
            check_opt=option.search([('name','=','ETIQ_PROD_EDITION'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_prod_edition = check.state 
            
            check_opt=option.search([('name','=','ETIQ_PROD_LIBELLE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_prod_libelle = check.state 
            
            check_opt=option.search([('name','=','ETIQ_PROD_LIB_ESPAGNOL'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_prod_lib_espagnol = check.state 
            
            check_opt=option.search([('name','=','ETIQ_PROD_LIB_LATIN'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_prod_lib_latin = check.state   

    if origin == 'Product' or origin == 'PriceList' :
            check_opt=option.search([('name','=','ETIQ_FORMAT'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_format = check.state 

            check_opt=option.search([('name','=','TARIF_OPTION'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_tarif_option = check.state 
            
            check_opt=option.search([('name','=','TARIF_CODE_INTERNE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_tarif_code_interne = check.state 
                        
            check_opt=option.search([('name','=','TARIF_REF_CLIENT'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_tarif_ref_client = check.state 

            check_opt=option.search([('name','=','TARIF_LIB_PROMO'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_tarif_lib_promo = check.state  

    # Partner
    if origin == 'Partner' or origin == 'PriceList' :
            check_opt=option.search([('name','=','GESTION_IFLS'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_ifls = check.state

    if origin == 'Partner' :
            check_opt=option.search([('name','=','REF_FRS'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_frs = check.state
            check_opt=option.search([('name','=','EDI_FACTURE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_edi_facture = check.state
            check_opt=option.search([('name','=','EDI_TRANSPORTEUR'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_edi_transporteur = check.state
            check_opt=option.search([('name','=','BL_VALORISE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_bl_valorise = check.state
            check_opt=option.search([('name','=','ETIQ_LOT_AUTO'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_lot_auto = check.state
            check_opt=option.search([('name','=','PRIX_KG'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_prix_kg = check.state
            check_opt=option.search([('name','=','TYPE_TIERS'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_type_tiers = check.state
            check_opt=option.search([('name','=','ETIQ_DLC'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_dlc = check.state
            check_opt=option.search([('name','=','ETIQ_COULEUR_CLIENT'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_couleur_client = check.state
            check_opt=option.search([('name','=','ETIQ_EAN_128'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_ean_128 = check.state
            check_opt=option.search([('name','=','ETIQ_TYPE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_etiq_type = check.state                                                                                                                                    
            check_opt=option.search([('name','=','EXPORT_COMPTA'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_export_compta = check.state  
            check_opt=option.search([('name','=','FONCTION_DEPORTE'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_fonction_deporte = check.state  
            check_opt=option.search([('name','=','REGR_PROD_FAC'),('company_id','=', self.company_id.id)])
            for check in check_opt:
                self.is_regr_prod_fac = check.state      


@api.model
def prepareprintlabel(self, nom_table, id_table):
        query = """SELECT to_char(sl.packaging_date,'DD/MM/YYYY'), to_char(sl.sending_date,'DD/MM/YYYY'), 
                    pt.etiq_description, pc.complete_name, 
                    hfc.name, hfp.name, pt.etiq_mention, 
                    sl.code_barre, sl.code_128, sl.qte,  
                    case sl.qte when 0 then sl.pds else sl.pds/sl.qte end,
                    sl.nb_mini, p.realname, p.adressip,l.file,
                    t.customer_name_etiq, t.customer_city_etiq, 
                    etab.health_number, etab.company_name_etiq, etab.company_city_etiq, etab.etiq_mention,
                    sl.numlot, sl.color_etiq, pt.etiq_latin, pt.etiq_spanish, pt.name, 
                    l.with_ean128, etab.compteur_ean128, etab.id
                    FROM """ + nom_table + """ sl
                    LEFT JOIN hubi_printer p ON sl.printer_id = p.id 
                    LEFT JOIN hubi_labelmodel l ON sl.label_id = l.id
                    INNER JOIN res_partner t ON t.id = sl.partner_id
                    LEFT JOIN res_partner etab ON etab.id = sl.etabexp_id
                    INNER JOIN product_product prod ON prod.id = sl.product_id
                    INNER JOIN product_template pt ON prod.product_tmpl_id = pt.id
                     INNER JOIN product_category pc ON pt.categ_id = pc.id 
                    INNER JOIN hubi_family AS hfc ON pt.caliber_id = hfc.id 
                    INNER JOIN hubi_family AS hfp ON pt.packaging_id = hfp.id 
                    WHERE sl.id=""" + str(id_table)
        self.env.cr.execute(query)
        
        result = [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27], r[28]) for r in self.env.cr.fetchall()]
        
        for packaging_date,sending_date,product_description, category_name,caliber_name,packaging_name,etiq_mention,code_barre,code128,qte,pds,nb_mini,printerName,adressip,labelFile,clientname1,clientname2,numsanitaire,etabexp1,etabexp2,etab_mention,lot,color,etiq_latin,etiq_spanish,product_name,with_ean128,compteur_ean128, etab_id in result:
            if (product_description is not None):
                description_item = product_description
            else:
                description_item = category_name  
                
            if (etiq_mention is not None):
                mention_item = etiq_mention
            else:
                mention_item = etab_mention  
                
            informations = [
                ("dateemb",packaging_date),
                ("dateexp",sending_date),
                ("produit",description_item),
                ("calibre",caliber_name),
                ("conditionnement",packaging_name),
                ("mention",mention_item),
                ("latin",etiq_latin),
                ("spanish",etiq_spanish),
                ("codebarre",code_barre),
                ("codeb128",code128),
                ("qte",int(qte)),
                ("pds",pds),
                ("nb",int(nb_mini)),
                ("numsanitaire",numsanitaire),
                ("client1", clientname1),
                ("client2", clientname2),
                ("etab1", etabexp1),
                ("etab2", etabexp2),
                ("lot", lot),
                ("color", color)]
            
            if(printerName is not None and printerName != "" and labelFile is not None and labelFile != ""):
                if (adressip is not None and adressip != ""):
                    printer = "\\\\" + adressip + "\\" + printerName
                else:
                    printer = printerName
                    
                ctrl_print.printlabelonwindows(printer,labelFile,'[',informations)   

                # Update counter of barcode 128
                if with_ean128:
                    if compteur_ean128:
                        compteur_ean128 += 1
                    else:
                        compteur_ean128 = 2    
                    req = """UPDATE res_partner SET compteur_ean128=%s  where id=%s"""
        
                    params = (compteur_ean128, etab_id)
                    self._cr.execute(req,params)
                    self.env.cr.commit()
                    
def calcul_cle_code_ean13(self, ean):
    # Calcul cle code ean13
    somme = 0
    coeff = "131313131313"

    for i in range(0,12):
        somme = somme + int(ean[i])*int(coeff[i])

    reste = somme % 10
    if reste == 0:
        cle = 0
    else: 
        cle = 10 - reste
        
    return "%s" % (cle) 

def replace_accent(self,s):
    if s:
        s = s.replace('ê', 'e') \
             .replace('è', 'e') \
             .replace('é', 'e') \
             .replace('à', 'a') \
             .replace('ô', 'o') \
             .replace('ö', 'o') \
             .replace('î', 'i')
    return s                 
                      
def left(aString, howMany):
    if howMany <1:
        return ''
    else:
        return aString[:howMany]

def right(aString, howMany):
    if howMany <1:
        return ''
    else:
        return aString[-howMany:]

def mid(aString, startChar, howMany):
    if howMany < 1:
        return ''
    else:
        return aString[startChar:startChar+howMany]