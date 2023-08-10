# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpEspAnswer(models.Model):
    ans_id = models.AutoField(db_column='ANS_ID', primary_key=True)  # Field name made lowercase.
    reg_id = models.PositiveIntegerField(db_column='REG_ID')  # Field name made lowercase.
    qst_id = models.PositiveIntegerField(db_column='QST_ID')  # Field name made lowercase.
    ans_value = models.TextField(db_column='ANS_value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_answer'


class WpEspAttendeeMeta(models.Model):
    attm_id = models.AutoField(db_column='ATTM_ID', primary_key=True)  # Field name made lowercase.
    att_id = models.BigIntegerField(db_column='ATT_ID')  # Field name made lowercase.
    att_fname = models.CharField(db_column='ATT_fname', max_length=45)  # Field name made lowercase.
    att_lname = models.CharField(db_column='ATT_lname', max_length=45)  # Field name made lowercase.
    att_address = models.CharField(db_column='ATT_address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    att_address2 = models.CharField(db_column='ATT_address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    att_city = models.CharField(db_column='ATT_city', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sta_id = models.IntegerField(db_column='STA_ID', blank=True, null=True)  # Field name made lowercase.
    cnt_iso = models.CharField(db_column='CNT_ISO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    att_zip = models.CharField(db_column='ATT_zip', max_length=12, blank=True, null=True)  # Field name made lowercase.
    att_email = models.CharField(db_column='ATT_email', max_length=255)  # Field name made lowercase.
    att_phone = models.CharField(db_column='ATT_phone', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_attendee_meta'


class WpEspCheckin(models.Model):
    chk_id = models.AutoField(db_column='CHK_ID', primary_key=True)  # Field name made lowercase.
    reg_id = models.PositiveIntegerField(db_column='REG_ID')  # Field name made lowercase.
    dtt_id = models.PositiveIntegerField(db_column='DTT_ID')  # Field name made lowercase.
    chk_in = models.PositiveIntegerField(db_column='CHK_in')  # Field name made lowercase.
    chk_timestamp = models.DateTimeField(db_column='CHK_timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_checkin'


class WpEspCountry(models.Model):
    cnt_iso = models.CharField(db_column='CNT_ISO', primary_key=True, max_length=2)  # Field name made lowercase.
    cnt_iso3 = models.CharField(db_column='CNT_ISO3', max_length=3)  # Field name made lowercase.
    rgn_id = models.PositiveIntegerField(db_column='RGN_ID', blank=True, null=True)  # Field name made lowercase.
    cnt_name = models.CharField(db_column='CNT_name', max_length=45)  # Field name made lowercase.
    cnt_cur_code = models.CharField(db_column='CNT_cur_code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cnt_cur_single = models.CharField(db_column='CNT_cur_single', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cnt_cur_plural = models.CharField(db_column='CNT_cur_plural', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cnt_cur_sign = models.CharField(db_column='CNT_cur_sign', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cnt_cur_sign_b4 = models.IntegerField(db_column='CNT_cur_sign_b4', blank=True, null=True)  # Field name made lowercase.
    cnt_cur_dec_plc = models.PositiveIntegerField(db_column='CNT_cur_dec_plc')  # Field name made lowercase.
    cnt_cur_dec_mrk = models.CharField(db_column='CNT_cur_dec_mrk', max_length=1)  # Field name made lowercase.
    cnt_cur_thsnds = models.CharField(db_column='CNT_cur_thsnds', max_length=1)  # Field name made lowercase.
    cnt_tel_code = models.CharField(db_column='CNT_tel_code', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cnt_is_eu = models.IntegerField(db_column='CNT_is_EU', blank=True, null=True)  # Field name made lowercase.
    cnt_active = models.IntegerField(db_column='CNT_active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_country'


class WpEspCurrency(models.Model):
    cur_code = models.CharField(db_column='CUR_code', primary_key=True, max_length=6)  # Field name made lowercase.
    cur_single = models.CharField(db_column='CUR_single', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cur_plural = models.CharField(db_column='CUR_plural', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cur_sign = models.CharField(db_column='CUR_sign', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cur_dec_plc = models.CharField(db_column='CUR_dec_plc', max_length=1)  # Field name made lowercase.
    cur_active = models.IntegerField(db_column='CUR_active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_currency'


class WpEspCurrencyPaymentMethod(models.Model):
    cpm_id = models.AutoField(db_column='CPM_ID', primary_key=True)  # Field name made lowercase.
    cur_code = models.CharField(db_column='CUR_code', max_length=6)  # Field name made lowercase.
    pmd_id = models.IntegerField(db_column='PMD_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_currency_payment_method'


class WpEspDatetime(models.Model):
    dtt_id = models.AutoField(db_column='DTT_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    dtt_name = models.CharField(db_column='DTT_name', max_length=255)  # Field name made lowercase.
    dtt_description = models.TextField(db_column='DTT_description')  # Field name made lowercase.
    dtt_evt_start = models.DateTimeField(db_column='DTT_EVT_start')  # Field name made lowercase.
    dtt_evt_end = models.DateTimeField(db_column='DTT_EVT_end')  # Field name made lowercase.
    dtt_reg_limit = models.IntegerField(db_column='DTT_reg_limit', blank=True, null=True)  # Field name made lowercase.
    dtt_sold = models.PositiveIntegerField(db_column='DTT_sold', blank=True, null=True)  # Field name made lowercase.
    dtt_reserved = models.PositiveSmallIntegerField(db_column='DTT_reserved')  # Field name made lowercase.
    dtt_is_primary = models.PositiveIntegerField(db_column='DTT_is_primary')  # Field name made lowercase.
    dtt_order = models.PositiveIntegerField(db_column='DTT_order', blank=True, null=True)  # Field name made lowercase.
    dtt_parent = models.PositiveIntegerField(db_column='DTT_parent', blank=True, null=True)  # Field name made lowercase.
    dtt_deleted = models.PositiveIntegerField(db_column='DTT_deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_datetime'


class WpEspDatetimeTicket(models.Model):
    dtk_id = models.AutoField(db_column='DTK_ID', primary_key=True)  # Field name made lowercase.
    dtt_id = models.PositiveIntegerField(db_column='DTT_ID')  # Field name made lowercase.
    tkt_id = models.PositiveIntegerField(db_column='TKT_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_datetime_ticket'


class WpEspEventMessageTemplate(models.Model):
    emt_id = models.BigAutoField(db_column='EMT_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    grp_id = models.PositiveIntegerField(db_column='GRP_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_event_message_template'


class WpEspEventMeta(models.Model):
    evtm_id = models.AutoField(db_column='EVTM_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    evt_display_desc = models.PositiveIntegerField(db_column='EVT_display_desc')  # Field name made lowercase.
    evt_display_ticket_selector = models.PositiveIntegerField(db_column='EVT_display_ticket_selector')  # Field name made lowercase.
    evt_visible_on = models.DateTimeField(db_column='EVT_visible_on')  # Field name made lowercase.
    evt_default_registration_status = models.CharField(db_column='EVT_default_registration_status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    evt_phone = models.CharField(db_column='EVT_phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    evt_additional_limit = models.PositiveIntegerField(db_column='EVT_additional_limit', blank=True, null=True)  # Field name made lowercase.
    evt_member_only = models.PositiveIntegerField(db_column='EVT_member_only')  # Field name made lowercase.
    evt_allow_overflow = models.PositiveIntegerField(db_column='EVT_allow_overflow')  # Field name made lowercase.
    evt_timezone_string = models.CharField(db_column='EVT_timezone_string', max_length=45, blank=True, null=True)  # Field name made lowercase.
    evt_external_url = models.CharField(db_column='EVT_external_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    evt_donations = models.IntegerField(db_column='EVT_donations', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_event_meta'


class WpEspEventQuestionGroup(models.Model):
    eqg_id = models.AutoField(db_column='EQG_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    qsg_id = models.PositiveIntegerField(db_column='QSG_ID')  # Field name made lowercase.
    eqg_primary = models.PositiveIntegerField(db_column='EQG_primary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_event_question_group'


class WpEspEventVenue(models.Model):
    evv_id = models.AutoField(db_column='EVV_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    vnu_id = models.BigIntegerField(db_column='VNU_ID')  # Field name made lowercase.
    evv_primary = models.PositiveIntegerField(db_column='EVV_primary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_event_venue'


class WpEspExtraJoin(models.Model):
    exj_id = models.AutoField(db_column='EXJ_ID', primary_key=True)  # Field name made lowercase.
    exj_first_model_id = models.CharField(db_column='EXJ_first_model_id', max_length=6)  # Field name made lowercase.
    exj_first_model_name = models.CharField(db_column='EXJ_first_model_name', max_length=20)  # Field name made lowercase.
    exj_second_model_id = models.CharField(db_column='EXJ_second_model_id', max_length=6)  # Field name made lowercase.
    exj_second_model_name = models.CharField(db_column='EXJ_second_model_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_extra_join'


class WpEspExtraMeta(models.Model):
    exm_id = models.AutoField(db_column='EXM_ID', primary_key=True)  # Field name made lowercase.
    obj_id = models.IntegerField(db_column='OBJ_ID', blank=True, null=True)  # Field name made lowercase.
    exm_type = models.CharField(db_column='EXM_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    exm_key = models.CharField(db_column='EXM_key', max_length=45, blank=True, null=True)  # Field name made lowercase.
    exm_value = models.TextField(db_column='EXM_value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_extra_meta'


class WpEspLineItem(models.Model):
    lin_id = models.AutoField(db_column='LIN_ID', primary_key=True)  # Field name made lowercase.
    lin_code = models.CharField(db_column='LIN_code', max_length=245)  # Field name made lowercase.
    txn_id = models.IntegerField(db_column='TXN_ID', blank=True, null=True)  # Field name made lowercase.
    lin_name = models.CharField(db_column='LIN_name', max_length=245)  # Field name made lowercase.
    lin_desc = models.TextField(db_column='LIN_desc', blank=True, null=True)  # Field name made lowercase.
    lin_unit_price = models.DecimalField(db_column='LIN_unit_price', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lin_percent = models.DecimalField(db_column='LIN_percent', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lin_is_taxable = models.IntegerField(db_column='LIN_is_taxable', blank=True, null=True)  # Field name made lowercase.
    lin_order = models.IntegerField(db_column='LIN_order', blank=True, null=True)  # Field name made lowercase.
    lin_parent = models.IntegerField(db_column='LIN_parent', blank=True, null=True)  # Field name made lowercase.
    lin_type = models.CharField(db_column='LIN_type', max_length=25)  # Field name made lowercase.
    lin_total = models.DecimalField(db_column='LIN_total', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lin_quantity = models.IntegerField(db_column='LIN_quantity', blank=True, null=True)  # Field name made lowercase.
    obj_id = models.IntegerField(db_column='OBJ_ID', blank=True, null=True)  # Field name made lowercase.
    obj_type = models.CharField(db_column='OBJ_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lin_timestamp = models.DateTimeField(db_column='LIN_timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_line_item'


class WpEspLog(models.Model):
    log_id = models.AutoField(db_column='LOG_ID', primary_key=True)  # Field name made lowercase.
    log_time = models.DateTimeField(db_column='LOG_time', blank=True, null=True)  # Field name made lowercase.
    obj_id = models.CharField(db_column='OBJ_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    obj_type = models.CharField(db_column='OBJ_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    log_type = models.CharField(db_column='LOG_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    log_message = models.TextField(db_column='LOG_message', blank=True, null=True)  # Field name made lowercase.
    log_wp_user = models.IntegerField(db_column='LOG_wp_user', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_log'


class WpEspMessage(models.Model):
    msg_id = models.BigAutoField(db_column='MSG_ID', primary_key=True)  # Field name made lowercase.
    grp_id = models.PositiveIntegerField(db_column='GRP_ID', blank=True, null=True)  # Field name made lowercase.
    msg_token = models.CharField(db_column='MSG_token', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txn_id = models.PositiveIntegerField(db_column='TXN_ID', blank=True, null=True)  # Field name made lowercase.
    msg_messenger = models.CharField(db_column='MSG_messenger', max_length=30)  # Field name made lowercase.
    msg_message_type = models.CharField(db_column='MSG_message_type', max_length=50)  # Field name made lowercase.
    msg_context = models.CharField(db_column='MSG_context', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msg_recipient_id = models.BigIntegerField(db_column='MSG_recipient_ID', blank=True, null=True)  # Field name made lowercase.
    msg_recipient_type = models.CharField(db_column='MSG_recipient_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    msg_content = models.TextField(db_column='MSG_content', blank=True, null=True)  # Field name made lowercase.
    msg_to = models.CharField(db_column='MSG_to', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msg_from = models.CharField(db_column='MSG_from', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msg_subject = models.CharField(db_column='MSG_subject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msg_priority = models.IntegerField(db_column='MSG_priority')  # Field name made lowercase.
    sts_id = models.CharField(db_column='STS_ID', max_length=3)  # Field name made lowercase.
    msg_created = models.DateTimeField(db_column='MSG_created')  # Field name made lowercase.
    msg_modified = models.DateTimeField(db_column='MSG_modified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_message'


class WpEspMessageTemplate(models.Model):
    mtp_id = models.AutoField(db_column='MTP_ID', primary_key=True)  # Field name made lowercase.
    grp_id = models.PositiveIntegerField(db_column='GRP_ID')  # Field name made lowercase.
    mtp_context = models.CharField(db_column='MTP_context', max_length=50)  # Field name made lowercase.
    mtp_template_field = models.CharField(db_column='MTP_template_field', max_length=30)  # Field name made lowercase.
    mtp_content = models.TextField(db_column='MTP_content')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_message_template'


class WpEspMessageTemplateGroup(models.Model):
    grp_id = models.AutoField(db_column='GRP_ID', primary_key=True)  # Field name made lowercase.
    mtp_user_id = models.IntegerField(db_column='MTP_user_id')  # Field name made lowercase.
    mtp_name = models.CharField(db_column='MTP_name', max_length=245)  # Field name made lowercase.
    mtp_description = models.CharField(db_column='MTP_description', max_length=245)  # Field name made lowercase.
    mtp_messenger = models.CharField(db_column='MTP_messenger', max_length=30)  # Field name made lowercase.
    mtp_message_type = models.CharField(db_column='MTP_message_type', max_length=50)  # Field name made lowercase.
    mtp_is_global = models.IntegerField(db_column='MTP_is_global')  # Field name made lowercase.
    mtp_is_override = models.IntegerField(db_column='MTP_is_override')  # Field name made lowercase.
    mtp_deleted = models.IntegerField(db_column='MTP_deleted')  # Field name made lowercase.
    mtp_is_active = models.IntegerField(db_column='MTP_is_active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_message_template_group'


class WpEspPayment(models.Model):
    pay_id = models.AutoField(db_column='PAY_ID', primary_key=True)  # Field name made lowercase.
    txn_id = models.PositiveIntegerField(db_column='TXN_ID', blank=True, null=True)  # Field name made lowercase.
    sts_id = models.CharField(db_column='STS_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pay_timestamp = models.DateTimeField(db_column='PAY_timestamp')  # Field name made lowercase.
    pay_source = models.CharField(db_column='PAY_source', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pay_amount = models.DecimalField(db_column='PAY_amount', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pmd_id = models.IntegerField(db_column='PMD_ID', blank=True, null=True)  # Field name made lowercase.
    pay_gateway_response = models.TextField(db_column='PAY_gateway_response', blank=True, null=True)  # Field name made lowercase.
    pay_txn_id_chq_nmbr = models.CharField(db_column='PAY_txn_id_chq_nmbr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pay_po_number = models.CharField(db_column='PAY_po_number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pay_extra_accntng = models.CharField(db_column='PAY_extra_accntng', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pay_details = models.TextField(db_column='PAY_details', blank=True, null=True)  # Field name made lowercase.
    pay_redirect_url = models.CharField(db_column='PAY_redirect_url', max_length=300, blank=True, null=True)  # Field name made lowercase.
    pay_redirect_args = models.TextField(db_column='PAY_redirect_args', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_payment'


class WpEspPaymentMethod(models.Model):
    pmd_id = models.AutoField(db_column='PMD_ID', primary_key=True)  # Field name made lowercase.
    pmd_type = models.CharField(db_column='PMD_type', max_length=124, blank=True, null=True)  # Field name made lowercase.
    pmd_name = models.CharField(db_column='PMD_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pmd_desc = models.TextField(db_column='PMD_desc', blank=True, null=True)  # Field name made lowercase.
    pmd_admin_name = models.CharField(db_column='PMD_admin_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pmd_admin_desc = models.TextField(db_column='PMD_admin_desc', blank=True, null=True)  # Field name made lowercase.
    pmd_slug = models.CharField(db_column='PMD_slug', unique=True, max_length=124, blank=True, null=True)  # Field name made lowercase.
    pmd_order = models.IntegerField(db_column='PMD_order', blank=True, null=True)  # Field name made lowercase.
    pmd_debug_mode = models.IntegerField(db_column='PMD_debug_mode')  # Field name made lowercase.
    pmd_wp_user = models.IntegerField(db_column='PMD_wp_user')  # Field name made lowercase.
    pmd_open_by_default = models.IntegerField(db_column='PMD_open_by_default')  # Field name made lowercase.
    pmd_button_url = models.CharField(db_column='PMD_button_url', max_length=1012, blank=True, null=True)  # Field name made lowercase.
    pmd_scope = models.CharField(db_column='PMD_scope', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_payment_method'


class WpEspPrice(models.Model):
    prc_id = models.AutoField(db_column='PRC_ID', primary_key=True)  # Field name made lowercase.
    prt_id = models.PositiveIntegerField(db_column='PRT_ID')  # Field name made lowercase.
    prc_amount = models.DecimalField(db_column='PRC_amount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    prc_name = models.CharField(db_column='PRC_name', max_length=245)  # Field name made lowercase.
    prc_desc = models.TextField(db_column='PRC_desc', blank=True, null=True)  # Field name made lowercase.
    prc_is_default = models.PositiveIntegerField(db_column='PRC_is_default')  # Field name made lowercase.
    prc_overrides = models.PositiveIntegerField(db_column='PRC_overrides', blank=True, null=True)  # Field name made lowercase.
    prc_deleted = models.PositiveIntegerField(db_column='PRC_deleted')  # Field name made lowercase.
    prc_order = models.PositiveIntegerField(db_column='PRC_order')  # Field name made lowercase.
    prc_wp_user = models.BigIntegerField(db_column='PRC_wp_user', blank=True, null=True)  # Field name made lowercase.
    prc_parent = models.PositiveIntegerField(db_column='PRC_parent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_price'


class WpEspPriceType(models.Model):
    prt_id = models.AutoField(db_column='PRT_ID', primary_key=True)  # Field name made lowercase.
    prt_name = models.CharField(db_column='PRT_name', unique=True, max_length=45)  # Field name made lowercase.
    pbt_id = models.PositiveIntegerField(db_column='PBT_ID')  # Field name made lowercase.
    prt_is_percent = models.IntegerField(db_column='PRT_is_percent')  # Field name made lowercase.
    prt_order = models.PositiveIntegerField(db_column='PRT_order', blank=True, null=True)  # Field name made lowercase.
    prt_wp_user = models.BigIntegerField(db_column='PRT_wp_user', blank=True, null=True)  # Field name made lowercase.
    prt_deleted = models.IntegerField(db_column='PRT_deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_price_type'


class WpEspQuestion(models.Model):
    qst_id = models.AutoField(db_column='QST_ID', primary_key=True)  # Field name made lowercase.
    qst_display_text = models.TextField(db_column='QST_display_text')  # Field name made lowercase.
    qst_admin_label = models.CharField(db_column='QST_admin_label', max_length=255)  # Field name made lowercase.
    qst_system = models.CharField(db_column='QST_system', max_length=25, blank=True, null=True)  # Field name made lowercase.
    qst_type = models.CharField(db_column='QST_type', max_length=25)  # Field name made lowercase.
    qst_required = models.PositiveIntegerField(db_column='QST_required')  # Field name made lowercase.
    qst_required_text = models.CharField(db_column='QST_required_text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qst_order = models.PositiveIntegerField(db_column='QST_order')  # Field name made lowercase.
    qst_admin_only = models.IntegerField(db_column='QST_admin_only')  # Field name made lowercase.
    qst_max = models.SmallIntegerField(db_column='QST_max')  # Field name made lowercase.
    qst_wp_user = models.BigIntegerField(db_column='QST_wp_user', blank=True, null=True)  # Field name made lowercase.
    qst_deleted = models.PositiveIntegerField(db_column='QST_deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_question'


class WpEspQuestionGroup(models.Model):
    qsg_id = models.AutoField(db_column='QSG_ID', primary_key=True)  # Field name made lowercase.
    qsg_name = models.CharField(db_column='QSG_name', max_length=255)  # Field name made lowercase.
    qsg_identifier = models.CharField(db_column='QSG_identifier', unique=True, max_length=100)  # Field name made lowercase.
    qsg_desc = models.TextField(db_column='QSG_desc', blank=True, null=True)  # Field name made lowercase.
    qsg_order = models.PositiveIntegerField(db_column='QSG_order')  # Field name made lowercase.
    qsg_show_group_name = models.IntegerField(db_column='QSG_show_group_name')  # Field name made lowercase.
    qsg_show_group_desc = models.IntegerField(db_column='QSG_show_group_desc')  # Field name made lowercase.
    qsg_system = models.IntegerField(db_column='QSG_system', blank=True, null=True)  # Field name made lowercase.
    qsg_deleted = models.PositiveIntegerField(db_column='QSG_deleted')  # Field name made lowercase.
    qsg_wp_user = models.BigIntegerField(db_column='QSG_wp_user', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_question_group'


class WpEspQuestionGroupQuestion(models.Model):
    qgq_id = models.AutoField(db_column='QGQ_ID', primary_key=True)  # Field name made lowercase.
    qsg_id = models.PositiveIntegerField(db_column='QSG_ID')  # Field name made lowercase.
    qst_id = models.PositiveIntegerField(db_column='QST_ID')  # Field name made lowercase.
    qgq_order = models.PositiveIntegerField(db_column='QGQ_order')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_question_group_question'


class WpEspQuestionOption(models.Model):
    qso_id = models.AutoField(db_column='QSO_ID', primary_key=True)  # Field name made lowercase.
    qso_value = models.CharField(db_column='QSO_value', max_length=255)  # Field name made lowercase.
    qso_desc = models.TextField(db_column='QSO_desc')  # Field name made lowercase.
    qst_id = models.PositiveIntegerField(db_column='QST_ID')  # Field name made lowercase.
    qso_order = models.PositiveIntegerField(db_column='QSO_order')  # Field name made lowercase.
    qso_system = models.CharField(db_column='QSO_system', max_length=25, blank=True, null=True)  # Field name made lowercase.
    qso_deleted = models.PositiveIntegerField(db_column='QSO_deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_question_option'


class WpEspRegistration(models.Model):
    reg_id = models.AutoField(db_column='REG_ID', primary_key=True)  # Field name made lowercase.
    evt_id = models.BigIntegerField(db_column='EVT_ID')  # Field name made lowercase.
    att_id = models.BigIntegerField(db_column='ATT_ID')  # Field name made lowercase.
    txn_id = models.PositiveIntegerField(db_column='TXN_ID')  # Field name made lowercase.
    tkt_id = models.PositiveIntegerField(db_column='TKT_ID')  # Field name made lowercase.
    sts_id = models.CharField(db_column='STS_ID', max_length=3)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_date')  # Field name made lowercase.
    reg_final_price = models.DecimalField(db_column='REG_final_price', max_digits=10, decimal_places=3)  # Field name made lowercase.
    reg_paid = models.DecimalField(db_column='REG_paid', max_digits=10, decimal_places=3)  # Field name made lowercase.
    reg_session = models.CharField(db_column='REG_session', max_length=45)  # Field name made lowercase.
    reg_code = models.CharField(db_column='REG_code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reg_url_link = models.CharField(db_column='REG_url_link', max_length=64, blank=True, null=True)  # Field name made lowercase.
    reg_count = models.PositiveIntegerField(db_column='REG_count', blank=True, null=True)  # Field name made lowercase.
    reg_group_size = models.PositiveIntegerField(db_column='REG_group_size', blank=True, null=True)  # Field name made lowercase.
    reg_att_is_going = models.IntegerField(db_column='REG_att_is_going', blank=True, null=True)  # Field name made lowercase.
    reg_deleted = models.IntegerField(db_column='REG_deleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_registration'


class WpEspRegistrationPayment(models.Model):
    rpy_id = models.AutoField(db_column='RPY_ID', primary_key=True)  # Field name made lowercase.
    reg_id = models.PositiveIntegerField(db_column='REG_ID')  # Field name made lowercase.
    pay_id = models.PositiveIntegerField(db_column='PAY_ID', blank=True, null=True)  # Field name made lowercase.
    rpy_amount = models.DecimalField(db_column='RPY_amount', max_digits=10, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_registration_payment'


class WpEspState(models.Model):
    sta_id = models.SmallAutoField(db_column='STA_ID', primary_key=True)  # Field name made lowercase.
    cnt_iso = models.CharField(db_column='CNT_ISO', max_length=2)  # Field name made lowercase.
    sta_abbrev = models.CharField(db_column='STA_abbrev', max_length=24)  # Field name made lowercase.
    sta_name = models.CharField(db_column='STA_name', max_length=100)  # Field name made lowercase.
    sta_active = models.IntegerField(db_column='STA_active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_state'


class WpEspStatus(models.Model):
    sts_id = models.CharField(db_column='STS_ID', unique=True, max_length=3)  # Field name made lowercase.
    sts_code = models.CharField(db_column='STS_code', max_length=45)  # Field name made lowercase.
    sts_type = models.CharField(db_column='STS_type', max_length=45)  # Field name made lowercase.
    sts_can_edit = models.IntegerField(db_column='STS_can_edit')  # Field name made lowercase.
    sts_desc = models.TextField(db_column='STS_desc', blank=True, null=True)  # Field name made lowercase.
    sts_open = models.IntegerField(db_column='STS_open')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_status'


class WpEspTicket(models.Model):
    tkt_id = models.AutoField(db_column='TKT_ID', primary_key=True)  # Field name made lowercase.
    ttm_id = models.PositiveIntegerField(db_column='TTM_ID')  # Field name made lowercase.
    tkt_name = models.CharField(db_column='TKT_name', max_length=245)  # Field name made lowercase.
    tkt_description = models.TextField(db_column='TKT_description')  # Field name made lowercase.
    tkt_qty = models.IntegerField(db_column='TKT_qty', blank=True, null=True)  # Field name made lowercase.
    tkt_sold = models.IntegerField(db_column='TKT_sold')  # Field name made lowercase.
    tkt_reserved = models.PositiveSmallIntegerField(db_column='TKT_reserved')  # Field name made lowercase.
    tkt_uses = models.IntegerField(db_column='TKT_uses')  # Field name made lowercase.
    tkt_required = models.PositiveIntegerField(db_column='TKT_required')  # Field name made lowercase.
    tkt_min = models.PositiveIntegerField(db_column='TKT_min')  # Field name made lowercase.
    tkt_max = models.IntegerField(db_column='TKT_max')  # Field name made lowercase.
    tkt_price = models.DecimalField(db_column='TKT_price', max_digits=10, decimal_places=3)  # Field name made lowercase.
    tkt_start_date = models.DateTimeField(db_column='TKT_start_date')  # Field name made lowercase.
    tkt_end_date = models.DateTimeField(db_column='TKT_end_date')  # Field name made lowercase.
    tkt_taxable = models.PositiveIntegerField(db_column='TKT_taxable')  # Field name made lowercase.
    tkt_order = models.PositiveIntegerField(db_column='TKT_order')  # Field name made lowercase.
    tkt_row = models.PositiveIntegerField(db_column='TKT_row')  # Field name made lowercase.
    tkt_is_default = models.PositiveIntegerField(db_column='TKT_is_default')  # Field name made lowercase.
    tkt_wp_user = models.BigIntegerField(db_column='TKT_wp_user', blank=True, null=True)  # Field name made lowercase.
    tkt_parent = models.PositiveIntegerField(db_column='TKT_parent', blank=True, null=True)  # Field name made lowercase.
    tkt_deleted = models.IntegerField(db_column='TKT_deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_ticket'


class WpEspTicketPrice(models.Model):
    tkp_id = models.AutoField(db_column='TKP_ID', primary_key=True)  # Field name made lowercase.
    tkt_id = models.PositiveIntegerField(db_column='TKT_ID')  # Field name made lowercase.
    prc_id = models.PositiveIntegerField(db_column='PRC_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_ticket_price'


class WpEspTicketTemplate(models.Model):
    ttm_id = models.AutoField(db_column='TTM_ID', primary_key=True)  # Field name made lowercase.
    ttm_name = models.CharField(db_column='TTM_name', max_length=45)  # Field name made lowercase.
    ttm_description = models.TextField(db_column='TTM_description', blank=True, null=True)  # Field name made lowercase.
    ttm_file = models.CharField(db_column='TTM_file', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_ticket_template'


class WpEspTransaction(models.Model):
    txn_id = models.AutoField(db_column='TXN_ID', primary_key=True)  # Field name made lowercase.
    txn_timestamp = models.DateTimeField(db_column='TXN_timestamp')  # Field name made lowercase.
    txn_total = models.DecimalField(db_column='TXN_total', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    txn_paid = models.DecimalField(db_column='TXN_paid', max_digits=10, decimal_places=3)  # Field name made lowercase.
    sts_id = models.CharField(db_column='STS_ID', max_length=3)  # Field name made lowercase.
    txn_session_data = models.TextField(db_column='TXN_session_data', blank=True, null=True)  # Field name made lowercase.
    txn_hash_salt = models.CharField(db_column='TXN_hash_salt', max_length=250, blank=True, null=True)  # Field name made lowercase.
    pmd_id = models.IntegerField(db_column='PMD_ID', blank=True, null=True)  # Field name made lowercase.
    txn_reg_steps = models.TextField(db_column='TXN_reg_steps', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_transaction'


class WpEspVenueMeta(models.Model):
    vnum_id = models.AutoField(db_column='VNUM_ID', primary_key=True)  # Field name made lowercase.
    vnu_id = models.BigIntegerField(db_column='VNU_ID')  # Field name made lowercase.
    vnu_address = models.CharField(db_column='VNU_address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vnu_address2 = models.CharField(db_column='VNU_address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vnu_city = models.CharField(db_column='VNU_city', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sta_id = models.IntegerField(db_column='STA_ID', blank=True, null=True)  # Field name made lowercase.
    cnt_iso = models.CharField(db_column='CNT_ISO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vnu_zip = models.CharField(db_column='VNU_zip', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vnu_phone = models.CharField(db_column='VNU_phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vnu_capacity = models.IntegerField(db_column='VNU_capacity', blank=True, null=True)  # Field name made lowercase.
    vnu_url = models.CharField(db_column='VNU_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vnu_virtual_phone = models.CharField(db_column='VNU_virtual_phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vnu_virtual_url = models.CharField(db_column='VNU_virtual_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vnu_enable_for_gmap = models.IntegerField(db_column='VNU_enable_for_gmap', blank=True, null=True)  # Field name made lowercase.
    vnu_google_map_link = models.CharField(db_column='VNU_google_map_link', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_esp_venue_meta'


class WpEwwwioImages(models.Model):
    id = models.AutoField(unique=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    gallery = models.CharField(max_length=10, blank=True, null=True)
    resize = models.CharField(max_length=75, blank=True, null=True)
    path = models.TextField()
    converted = models.TextField()
    results = models.CharField(max_length=75)
    image_size = models.PositiveIntegerField(blank=True, null=True)
    orig_size = models.PositiveIntegerField(blank=True, null=True)
    backup = models.CharField(max_length=100, blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    pending = models.IntegerField()
    updates = models.PositiveIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    trace = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_ewwwio_images'


class WpEwwwioQueue(models.Model):
    attachment_id = models.BigIntegerField(blank=True, null=True)
    gallery = models.CharField(max_length=10, blank=True, null=True)
    scanned = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_ewwwio_queue'


class WpFacetwpIndex(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveIntegerField(blank=True, null=True)
    facet_name = models.CharField(max_length=255, blank=True, null=True)
    facet_source = models.CharField(max_length=255, blank=True, null=True)
    facet_value = models.TextField(blank=True, null=True)
    facet_display_value = models.TextField(blank=True, null=True)
    term_id = models.PositiveIntegerField(blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    depth = models.PositiveIntegerField(blank=True, null=True)
    variation_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_facetwp_index'


class WpFullstripePaymentForms(models.Model):
    paymentformid = models.AutoField(db_column='paymentFormID', unique=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    formtitle = models.CharField(db_column='formTitle', max_length=100)  # Field name made lowercase.
    amount = models.IntegerField()
    customamount = models.IntegerField(db_column='customAmount', blank=True, null=True)  # Field name made lowercase.
    buttontitle = models.CharField(db_column='buttonTitle', max_length=100)  # Field name made lowercase.
    showbuttonamount = models.IntegerField(db_column='showButtonAmount', blank=True, null=True)  # Field name made lowercase.
    showemailinput = models.IntegerField(db_column='showEmailInput', blank=True, null=True)  # Field name made lowercase.
    showcustominput = models.IntegerField(db_column='showCustomInput', blank=True, null=True)  # Field name made lowercase.
    custominputtitle = models.CharField(db_column='customInputTitle', max_length=100)  # Field name made lowercase.
    redirectonsuccess = models.IntegerField(db_column='redirectOnSuccess', blank=True, null=True)  # Field name made lowercase.
    redirecturl = models.CharField(db_column='redirectUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    redirecttopageorpost = models.IntegerField(db_column='redirectToPageOrPost', blank=True, null=True)  # Field name made lowercase.
    redirectpostid = models.IntegerField(db_column='redirectPostID', blank=True, null=True)  # Field name made lowercase.
    showaddress = models.IntegerField(db_column='showAddress', blank=True, null=True)  # Field name made lowercase.
    sendemailreceipt = models.IntegerField(db_column='sendEmailReceipt', blank=True, null=True)  # Field name made lowercase.
    formstyle = models.IntegerField(db_column='formStyle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_fullstripe_payment_forms'


class WpFullstripePayments(models.Model):
    paymentid = models.AutoField(db_column='paymentID', unique=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=100)  # Field name made lowercase.
    description = models.CharField(max_length=255)
    paid = models.IntegerField(blank=True, null=True)
    livemode = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField()
    fee = models.IntegerField()
    addressline1 = models.CharField(db_column='addressLine1', max_length=500)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=500)  # Field name made lowercase.
    addresscity = models.CharField(db_column='addressCity', max_length=500)  # Field name made lowercase.
    addressstate = models.CharField(db_column='addressState', max_length=255)  # Field name made lowercase.
    addresszip = models.CharField(db_column='addressZip', max_length=100)  # Field name made lowercase.
    addresscountry = models.CharField(db_column='addressCountry', max_length=100)  # Field name made lowercase.
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_fullstripe_payments'


class WpGmpIcons(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gmp_icons'


class WpGmpMaps(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    html_options = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gmp_maps'


class WpGmpMarkerGroups(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_gmp_marker_groups'


class WpGmpMarkers(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField(blank=True, null=True)
    coord_x = models.CharField(max_length=30)
    coord_y = models.CharField(max_length=30)
    icon = models.IntegerField(blank=True, null=True)
    map_id = models.IntegerField(blank=True, null=True)
    marker_group_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    animation = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    params = models.TextField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_gmp_markers'


class WpGmpModules(models.Model):
    code = models.CharField(unique=True, max_length=64)
    active = models.IntegerField()
    type_id = models.SmallIntegerField()
    params = models.TextField(blank=True, null=True)
    has_tab = models.IntegerField()
    label = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ex_plug_dir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gmp_modules'


class WpGmpModulesType(models.Model):
    label = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'wp_gmp_modules_type'


class WpGmpOptions(models.Model):
    code = models.CharField(unique=True, max_length=64)
    value = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    htmltype_id = models.SmallIntegerField()
    params = models.TextField(blank=True, null=True)
    cat_id = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    value_type = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gmp_options'


class WpGmpOptionsCategories(models.Model):
    label = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'wp_gmp_options_categories'


class WpGmpUsageStat(models.Model):
    code = models.CharField(unique=True, max_length=64)
    visits = models.IntegerField()
    spent_time = models.IntegerField()
    modify_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_gmp_usage_stat'


class WpGmtrData(models.Model):
    id = models.BigAutoField(primary_key=True)
    gid = models.BigIntegerField(blank=True, null=True)
    orderid = models.BigIntegerField(blank=True, null=True)
    gmaps_address = models.TextField(blank=True, null=True)
    gmaps_title = models.CharField(max_length=200, blank=True, null=True)
    gmaps_description = models.TextField(blank=True, null=True)
    gmaps_url = models.CharField(max_length=200, blank=True, null=True)
    gmaps_lat_log = models.CharField(max_length=50, blank=True, null=True)
    gmaps_icon = models.CharField(max_length=200, blank=True, null=True)
    gmaps_infowindow_custom = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_gmtr_data'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpNf3ActionMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_action_meta'


class WpNf3Actions(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_actions'


class WpNf3FieldMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_field_meta'


class WpNf3Fields(models.Model):
    id = models.AutoField(unique=True)
    label = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_fields'


class WpNf3FormMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_form_meta'


class WpNf3Forms(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    subs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_forms'


class WpNf3ObjectMeta(models.Model):
    id = models.AutoField(unique=True)
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_object_meta'


class WpNf3Objects(models.Model):
    id = models.AutoField(unique=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_objects'


class WpNf3Relationships(models.Model):
    id = models.AutoField(unique=True)
    child_id = models.IntegerField()
    child_type = models.TextField()
    parent_id = models.IntegerField()
    parent_type = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_relationships'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191, blank=True, null=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpPrliClicks(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    btype = models.CharField(max_length=255, blank=True, null=True)
    bversion = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    robot = models.IntegerField(blank=True, null=True)
    first_click = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    link_id = models.IntegerField(blank=True, null=True)
    vuid = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_prli_clicks'


class WpPrliGroups(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_prli_groups'


class WpPrliLinkMetas(models.Model):
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)
    link_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_prli_link_metas'


class WpPrliLinks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    nofollow = models.IntegerField(blank=True, null=True)
    track_me = models.IntegerField(blank=True, null=True)
    param_forwarding = models.CharField(max_length=255, blank=True, null=True)
    param_struct = models.CharField(max_length=255, blank=True, null=True)
    redirect_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    group_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_prli_links'


class WpRevsliderCss(models.Model):
    id = models.AutoField(unique=True)
    handle = models.TextField()
    settings = models.TextField(blank=True, null=True)
    hover = models.TextField(blank=True, null=True)
    params = models.TextField()
    advanced = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_css'


class WpRevsliderLayerAnimations(models.Model):
    id = models.AutoField(unique=True)
    handle = models.TextField()
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_layer_animations'


class WpRevsliderNavigations(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=191)
    handle = models.CharField(max_length=191)
    css = models.TextField()
    markup = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_navigations'


class WpRevsliderSliders(models.Model):
    id = models.AutoField(unique=True)
    title = models.TextField()
    alias = models.TextField(blank=True, null=True)
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'wp_revslider_sliders'


class WpRevsliderSlides(models.Model):
    id = models.AutoField(unique=True)
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_slides'


class WpRevsliderStaticSlides(models.Model):
    id = models.AutoField(unique=True)
    slider_id = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_static_slides'


class WpRmFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    form_id = models.IntegerField(blank=True, null=True)
    page_no = models.PositiveIntegerField()
    field_label = models.TextField(blank=True, null=True)
    field_type = models.TextField(blank=True, null=True)
    field_value = models.TextField(blank=True, null=True)
    field_order = models.IntegerField(blank=True, null=True)
    field_show_on_user_page = models.IntegerField(blank=True, null=True)
    is_field_primary = models.IntegerField()
    field_is_editable = models.IntegerField()
    field_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_fields'


class WpRmForms(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=1000, blank=True, null=True)
    form_type = models.IntegerField(blank=True, null=True)
    form_user_role = models.CharField(max_length=1000, blank=True, null=True)
    default_user_role = models.CharField(max_length=255, blank=True, null=True)
    form_should_send_email = models.IntegerField(blank=True, null=True)
    form_redirect = models.CharField(max_length=10, blank=True, null=True)
    form_redirect_to_page = models.CharField(max_length=500, blank=True, null=True)
    form_redirect_to_url = models.CharField(max_length=500, blank=True, null=True)
    form_should_auto_expire = models.IntegerField(blank=True, null=True)
    form_options = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_forms'


class WpRmFrontUsers(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    otp_code = models.CharField(max_length=255)
    last_activity_time = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_front_users'


class WpRmNotes(models.Model):
    note_id = models.AutoField(primary_key=True)
    submission_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateTimeField()
    published_by = models.BigIntegerField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edited_by = models.BigIntegerField(blank=True, null=True)
    note_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_notes'


class WpRmPaypalFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=256, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    option_label = models.TextField(blank=True, null=True)
    option_price = models.TextField(blank=True, null=True)
    option_value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    require = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    extra_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_paypal_fields'


class WpRmPaypalLogs(models.Model):
    submission_id = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    txn_id = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    posted_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_paypal_logs'


class WpRmSentMails(models.Model):
    mail_id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    to = models.CharField(max_length=255, blank=True, null=True)
    sub = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    sent_on = models.DateTimeField(blank=True, null=True)
    headers = models.CharField(max_length=255, blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    exdata = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_sent_mails'


class WpRmSessions(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    data = models.TextField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_rm_sessions'


class WpRmStats(models.Model):
    stat_id = models.AutoField(primary_key=True)
    form_id = models.IntegerField(blank=True, null=True)
    user_ip = models.CharField(max_length=20, blank=True, null=True)
    ua_string = models.CharField(max_length=255, blank=True, null=True)
    browser_name = models.CharField(max_length=50, blank=True, null=True)
    visited_on = models.CharField(max_length=50, blank=True, null=True)
    submitted_on = models.CharField(max_length=50, blank=True, null=True)
    time_taken = models.IntegerField(blank=True, null=True)
    submission_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_stats'


class WpRmSubmissionFields(models.Model):
    sub_field_id = models.AutoField(primary_key=True)
    submission_id = models.IntegerField(blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_submission_fields'


class WpRmSubmissions(models.Model):
    submission_id = models.AutoField(primary_key=True)
    form_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    user_email = models.CharField(max_length=250, blank=True, null=True)
    child_id = models.IntegerField()
    last_child = models.IntegerField()
    is_read = models.IntegerField()
    submitted_on = models.DateTimeField(blank=True, null=True)
    unique_token = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_rm_submissions'


class WpSmsSend(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    sender = models.CharField(max_length=20)
    message = models.TextField()
    recipient = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_sms_send'


class WpSmsSubscribes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    status = models.IntegerField(blank=True, null=True)
    activate_key = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(db_column='group_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_sms_subscribes'


class WpSmsSubscribesGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_sms_subscribes_group'


class WpStrongViews(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_strong_views'


class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpTmTaskmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_tm_taskmeta'


class WpTmTasks(models.Model):
    user_id = models.BigIntegerField()
    type = models.CharField(max_length=300)
    class_identifier = models.CharField(max_length=300, blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    time_created = models.DateTimeField()
    last_locked_at = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_tm_tasks'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWfbadleechers(models.Model):
    emin = models.PositiveIntegerField(db_column='eMin', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfBadLeechers'
        unique_together = (('emin', 'ip'),)


class WpWfblockedcommentlog(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2)  # Field name made lowercase.
    blockcount = models.PositiveIntegerField(db_column='blockCount')  # Field name made lowercase.
    unixday = models.PositiveIntegerField()
    blocktype = models.CharField(db_column='blockType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfBlockedCommentLog'
        unique_together = (('ip', 'unixday', 'blocktype'),)


class WpWfblockediplog(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2)  # Field name made lowercase.
    blockcount = models.PositiveIntegerField(db_column='blockCount')  # Field name made lowercase.
    unixday = models.PositiveIntegerField()
    blocktype = models.CharField(db_column='blockType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfBlockedIPLog'
        unique_together = (('ip', 'unixday', 'blocktype'),)


class WpWfblocks7(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.PositiveIntegerField()
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    blockedtime = models.BigIntegerField(db_column='blockedTime')  # Field name made lowercase.
    reason = models.CharField(max_length=255)
    lastattempt = models.PositiveIntegerField(db_column='lastAttempt', blank=True, null=True)  # Field name made lowercase.
    blockedhits = models.PositiveIntegerField(db_column='blockedHits', blank=True, null=True)  # Field name made lowercase.
    expiration = models.BigIntegerField()
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfBlocks7'


class WpWfconfig(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    val = models.TextField(blank=True, null=True)
    autoload = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wp_wfConfig'


class WpWfcrawlers(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    patternsig = models.CharField(db_column='patternSig', max_length=16)  # Field name made lowercase.
    status = models.CharField(max_length=8)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.
    ptr = models.CharField(db_column='PTR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfCrawlers'
        unique_together = (('ip', 'patternsig'),)


class WpWffilechanges(models.Model):
    filenamehash = models.CharField(db_column='filenameHash', primary_key=True, max_length=64)  # Field name made lowercase.
    file = models.CharField(max_length=1000)
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_wfFileChanges'


class WpWffilemods(models.Model):
    filenamemd5 = models.CharField(db_column='filenameMD5', primary_key=True, max_length=16)  # Field name made lowercase.
    filename = models.CharField(max_length=1000)
    knownfile = models.PositiveIntegerField(db_column='knownFile')  # Field name made lowercase.
    oldmd5 = models.CharField(db_column='oldMD5', max_length=16)  # Field name made lowercase.
    newmd5 = models.CharField(db_column='newMD5', max_length=16)  # Field name made lowercase.
    shac = models.CharField(db_column='SHAC', max_length=32)  # Field name made lowercase.
    stoppedonsignature = models.CharField(db_column='stoppedOnSignature', max_length=255)  # Field name made lowercase.
    stoppedonposition = models.PositiveIntegerField(db_column='stoppedOnPosition')  # Field name made lowercase.
    issafefile = models.CharField(db_column='isSafeFile', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfFileMods'


class WpWfhits(models.Model):
    attacklogtime = models.FloatField(db_column='attackLogTime')  # Field name made lowercase.
    ctime = models.FloatField()
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    jsrun = models.IntegerField(db_column='jsRun', blank=True, null=True)  # Field name made lowercase.
    statuscode = models.IntegerField(db_column='statusCode')  # Field name made lowercase.
    isgoogle = models.IntegerField(db_column='isGoogle')  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    newvisit = models.PositiveIntegerField(db_column='newVisit')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    referer = models.TextField(blank=True, null=True)
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(max_length=64)
    actiondescription = models.TextField(db_column='actionDescription', blank=True, null=True)  # Field name made lowercase.
    actiondata = models.TextField(db_column='actionData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfHits'


class WpWfhoover(models.Model):
    owner = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    hostkey = models.CharField(db_column='hostKey', max_length=124, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfHoover'


class WpWfissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfIssues'


class WpWfknownfilelist(models.Model):
    path = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfKnownFileList'


class WpWfleechers(models.Model):
    emin = models.PositiveIntegerField(db_column='eMin', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfLeechers'
        unique_together = (('emin', 'ip'),)


class WpWflivetraffichuman(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    identifier = models.CharField(max_length=32)
    expiration = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfLiveTrafficHuman'
        unique_together = (('ip', 'identifier'),)


class WpWflocs(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    ctime = models.PositiveIntegerField()
    failed = models.PositiveIntegerField()
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    countryname = models.CharField(db_column='countryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfLocs'


class WpWflogins(models.Model):
    hitid = models.IntegerField(db_column='hitID', blank=True, null=True)  # Field name made lowercase.
    ctime = models.FloatField()
    fail = models.PositiveIntegerField()
    action = models.CharField(max_length=40)
    username = models.CharField(max_length=255)
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfLogins'


class WpWfnet404S(models.Model):
    sig = models.CharField(primary_key=True, max_length=16)
    ctime = models.PositiveIntegerField()
    uri = models.CharField(db_column='URI', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfNet404s'


class WpWfnotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    new = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    priority = models.IntegerField()
    ctime = models.PositiveIntegerField()
    html = models.TextField()
    links = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfNotifications'


class WpWfpendingissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfPendingIssues'


class WpWfreversecache(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    host = models.CharField(max_length=255)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfReverseCache'


class WpWfsnipcache(models.Model):
    ip = models.CharField(db_column='IP', max_length=45)  # Field name made lowercase.
    expiration = models.DateTimeField()
    body = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfSNIPCache'


class WpWfscanners(models.Model):
    emin = models.PositiveIntegerField(db_column='eMin', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    hits = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfScanners'
        unique_together = (('emin', 'ip'),)


class WpWfstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    ctime = models.FloatField()
    level = models.PositiveIntegerField()
    type = models.CharField(max_length=5)
    msg = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'wp_wfStatus'


class WpWfvulnscanners(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    ctime = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfVulnScanners'


class WpWplcChatMsgs(models.Model):
    chat_sess_id = models.IntegerField()
    msgfrom = models.CharField(max_length=150)
    msg = models.TextField()
    timestamp = models.DateTimeField()
    status = models.IntegerField()
    originates = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wplc_chat_msgs'


class WpWplcChatSessions(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=700)
    email = models.CharField(max_length=700)
    ip = models.CharField(max_length=700)
    status = models.IntegerField()
    session = models.CharField(max_length=100)
    url = models.CharField(max_length=700)
    last_active_timestamp = models.DateTimeField()
    other = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wplc_chat_sessions'


class WpWplcOfflineMessages(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=700)
    email = models.CharField(max_length=700)
    message = models.CharField(max_length=700)
    ip = models.CharField(max_length=700)
    user_agent = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'wp_wplc_offline_messages'


class WpYoastSeoLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    post_id = models.BigIntegerField()
    target_post_id = models.BigIntegerField()
    type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'wp_yoast_seo_links'


class WpYoastSeoMeta(models.Model):
    object_id = models.BigIntegerField(unique=True)
    internal_link_count = models.PositiveIntegerField(blank=True, null=True)
    incoming_link_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_seo_meta'
