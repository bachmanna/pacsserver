# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Code(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code_meaning = models.CharField(max_length=255)
    code_value = models.CharField(max_length=255)
    code_designator = models.CharField(max_length=255)
    code_version = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'code'
        unique_together = (('code_value', 'code_designator', 'code_version'),)


class ContentItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rel_type = models.CharField(max_length=255)
    text_value = models.CharField(max_length=255, blank=True, null=True)
    code_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='code_fk', blank=True, null=True, related_name='name_fk')
    name_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='name_fk')
    instance_fk = models.ForeignKey('Instance', models.DO_NOTHING, db_column='instance_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_item'


class Dicomattrs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attrs = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'dicomattrs'


class DiffTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    check_different = models.BooleanField()
    check_missing = models.BooleanField()
    compare_fields = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    different = models.IntegerField()
    local_aet = models.CharField(max_length=255)
    matches = models.IntegerField()
    missing = models.IntegerField()
    primary_aet = models.CharField(max_length=255)
    query_str = models.CharField(max_length=255)
    secondary_aet = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    queue_msg_fk = models.ForeignKey('QueueMsg', models.DO_NOTHING, db_column='queue_msg_fk', verbose_name="QueueMsg")

    class Meta:
        managed = False
        db_table = 'diff_task'


class DiffTaskAttrs(models.Model):
    diff_task_fk = models.ForeignKey(DiffTask, models.DO_NOTHING, db_column='diff_task_fk')
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")

    class Meta:
        managed = False
        db_table = 'diff_task_attrs'


class ExportTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_time = models.DateTimeField()
    device_name = models.CharField(max_length=255)
    exporter_id = models.CharField(max_length=255)
    modalities = models.CharField(max_length=255, blank=True, null=True)
    num_instances = models.IntegerField(blank=True, null=True)
    scheduled_time = models.DateTimeField()
    series_iuid = models.CharField(max_length=255)
    sop_iuid = models.CharField(max_length=255)
    study_iuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    queue_msg_fk = models.ForeignKey('QueueMsg', models.DO_NOTHING, db_column='queue_msg_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_task'


class Hl7PsuTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aet = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    device_name = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField(blank=True, null=True)
    study_iuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    mpps_fk = models.ForeignKey('Mpps', models.DO_NOTHING, db_column='mpps_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hl7psu_task'


class IanTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    calling_aet = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    ian_dests = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField(blank=True, null=True)
    study_iuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    mpps_fk = models.ForeignKey('Mpps', models.DO_NOTHING, db_column='mpps_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ian_task'


class IdSequence(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    next_value = models.IntegerField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id_sequence'


class Instance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    availability = models.IntegerField()
    sr_complete = models.CharField(max_length=255)
    content_date = models.CharField(max_length=255)
    content_time = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    ext_retrieve_aet = models.CharField(max_length=255, blank=True, null=True)
    inst_custom1 = models.CharField(max_length=255)
    inst_custom2 = models.CharField(max_length=255)
    inst_custom3 = models.CharField(max_length=255)
    inst_no = models.IntegerField(blank=True, null=True)
    num_frames = models.IntegerField(blank=True, null=True)
    retrieve_aets = models.CharField(max_length=255, blank=True, null=True)
    sop_cuid = models.CharField(max_length=255)
    sop_iuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    sr_verified = models.CharField(max_length=255)
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    srcode_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='srcode_fk', blank=True, null=True, related_name='srcode_fk')
    reject_code_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='reject_code_fk', blank=True, null=True)
    series_fk = models.ForeignKey('Series', models.DO_NOTHING, db_column='series_fk')

    class Meta:
        managed = False
        db_table = 'instance'
        unique_together = (('series_fk', 'sop_iuid'),)


class Issuer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    entity_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    entity_uid = models.CharField(max_length=255, blank=True, null=True)
    entity_uid_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issuer'
        unique_together = (('entity_uid', 'entity_uid_type'),)


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_time = models.DateTimeField()
    digest = models.CharField(max_length=255, blank=True, null=True)
    multi_ref = models.IntegerField(blank=True, null=True)
    object_type = models.IntegerField()
    object_size = models.BigIntegerField()
    status = models.IntegerField()
    storage_id = models.CharField(max_length=255)
    storage_path = models.CharField(max_length=255)
    tsuid = models.CharField(max_length=255, blank=True, null=True)
    instance_fk = models.ForeignKey(Instance, models.DO_NOTHING, db_column='instance_fk', blank=True, null=True)
    uidmap_fk = models.ForeignKey('Uidmap', models.DO_NOTHING, db_column='uidmap_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Metadata(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_time = models.DateTimeField()
    digest = models.CharField(max_length=255, blank=True, null=True)
    object_size = models.BigIntegerField()
    status = models.IntegerField()
    storage_id = models.CharField(max_length=255)
    storage_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'metadata'


class Mpps(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accession_no = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    pps_start_date = models.CharField(max_length=255)
    pps_start_time = models.CharField(max_length=255)
    sop_iuid = models.CharField(unique=True, max_length=255)
    pps_status = models.IntegerField()
    study_iuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    discreason_code_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='discreason_code_fk', blank=True, null=True)
    accno_issuer_fk = models.ForeignKey(Issuer, models.DO_NOTHING, db_column='accno_issuer_fk', blank=True, null=True)
    patient_fk = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_fk')

    class Meta:
        managed = False
        db_table = 'mpps'


class MwlItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accession_no = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modality = models.CharField(max_length=255)
    req_proc_id = models.CharField(max_length=255)
    sps_id = models.CharField(max_length=255)
    sps_start_date = models.CharField(max_length=255)
    sps_start_time = models.CharField(max_length=255)
    sps_status = models.IntegerField()
    study_iuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    accno_issuer_fk = models.ForeignKey(Issuer, models.DO_NOTHING, db_column='accno_issuer_fk', blank=True, null=True)
    patient_fk = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_fk')
    perf_phys_name_fk = models.ForeignKey('PersonName', models.DO_NOTHING, db_column='perf_phys_name_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mwl_item'
        unique_together = (('study_iuid', 'sps_id'),)


class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_time = models.DateTimeField()
    failed_verifications = models.IntegerField()
    num_studies = models.IntegerField()
    pat_birthdate = models.CharField(max_length=255)
    pat_custom1 = models.CharField(max_length=255)
    pat_custom2 = models.CharField(max_length=255)
    pat_custom3 = models.CharField(max_length=255)
    pat_sex = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    verification_status = models.IntegerField()
    verification_time = models.DateTimeField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    merge_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='merge_fk', blank=True, null=True)
    patient_id_fk = models.ForeignKey('PatientId', models.DO_NOTHING, db_column='patient_id_fk', verbose_name="PatientId", blank=True, null=True)
    pat_name_fk = models.ForeignKey('PersonName', models.DO_NOTHING, db_column='pat_name_fk', blank=True, null=True, related_name='resp_person_fk')
    resp_person_fk = models.ForeignKey('PersonName', models.DO_NOTHING, db_column='resp_person_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class PatientId(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pat_id = models.CharField(max_length=255)
    pat_id_type_code = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    issuer_fk = models.ForeignKey(Issuer, models.DO_NOTHING, db_column='issuer_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_id'
        unique_together = (('pat_id', 'issuer_fk'),)


class PersonName(models.Model):
    id = models.BigIntegerField(primary_key=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    i_family_name = models.CharField(max_length=255, blank=True, null=True)
    i_given_name = models.CharField(max_length=255, blank=True, null=True)
    i_middle_name = models.CharField(max_length=255, blank=True, null=True)
    i_name_prefix = models.CharField(max_length=255, blank=True, null=True)
    i_name_suffix = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    name_prefix = models.CharField(max_length=255, blank=True, null=True)
    name_suffix = models.CharField(max_length=255, blank=True, null=True)
    p_family_name = models.CharField(max_length=255, blank=True, null=True)
    p_given_name = models.CharField(max_length=255, blank=True, null=True)
    p_middle_name = models.CharField(max_length=255, blank=True, null=True)
    p_name_prefix = models.CharField(max_length=255, blank=True, null=True)
    p_name_suffix = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_name'


class QueueMsg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    device_name = models.CharField(max_length=255)
    error_msg = models.CharField(max_length=255, blank=True, null=True)
    msg_body = models.BinaryField()
    msg_id = models.CharField(unique=True, max_length=255)
    msg_props = models.CharField(max_length=4000)
    num_failures = models.IntegerField()
    outcome_msg = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    proc_end_time = models.DateTimeField(blank=True, null=True)
    proc_start_time = models.DateTimeField(blank=True, null=True)
    queue_name = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    msg_status = models.IntegerField()
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue_msg'


class RelStudyPcode(models.Model):
    study_fk = models.ForeignKey('Study', models.DO_NOTHING, db_column='study_fk')
    pcode_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='pcode_fk')

    class Meta:
        managed = False
        db_table = 'rel_study_pcode'


class RetrieveTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    completed = models.IntegerField()
    created_time = models.DateTimeField()
    destination_aet = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    error_comment = models.CharField(max_length=255, blank=True, null=True)
    failed = models.IntegerField()
    local_aet = models.CharField(max_length=255)
    queue_name = models.CharField(max_length=255)
    remaining = models.IntegerField()
    remote_aet = models.CharField(max_length=255)
    series_iuid = models.CharField(max_length=255, blank=True, null=True)
    sop_iuid = models.CharField(max_length=255, blank=True, null=True)
    status_code = models.IntegerField()
    study_iuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    warning = models.IntegerField()
    queue_msg_fk = models.ForeignKey(QueueMsg, models.DO_NOTHING, db_column='queue_msg_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retrieve_task'


class Series(models.Model):
    id = models.BigIntegerField(primary_key=True)
    body_part = models.CharField(max_length=255)
    completeness = models.IntegerField()
    compress_failures = models.IntegerField()
    compress_params = models.CharField(max_length=255, blank=True, null=True)
    compress_time = models.DateTimeField(blank=True, null=True)
    compress_tsuid = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    expiration_exporter_id = models.CharField(max_length=255, blank=True, null=True)
    expiration_state = models.IntegerField()
    ext_retrieve_aet = models.CharField(max_length=255, blank=True, null=True)
    failed_retrieves = models.IntegerField()
    stgver_failures = models.IntegerField()
    inst_purge_state = models.IntegerField()
    inst_purge_time = models.DateTimeField(blank=True, null=True)
    institution = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    laterality = models.CharField(max_length=255)
    metadata_update_time = models.DateTimeField(blank=True, null=True)
    metadata_update_failures = models.IntegerField()
    modality = models.CharField(max_length=255)
    pps_cuid = models.CharField(max_length=255)
    pps_iuid = models.CharField(max_length=255)
    pps_start_date = models.CharField(max_length=255)
    pps_start_time = models.CharField(max_length=255)
    rejection_state = models.IntegerField()
    series_custom1 = models.CharField(max_length=255)
    series_custom2 = models.CharField(max_length=255)
    series_custom3 = models.CharField(max_length=255)
    series_desc = models.CharField(max_length=255)
    series_iuid = models.CharField(max_length=255)
    series_no = models.IntegerField(blank=True, null=True)
    series_size = models.BigIntegerField()
    sop_cuid = models.CharField(max_length=255)
    src_aet = models.CharField(max_length=255, blank=True, null=True)
    station_name = models.CharField(max_length=255)
    stgver_time = models.DateTimeField(blank=True, null=True)
    tsuid = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    inst_code_fk = models.ForeignKey(Code, models.DO_NOTHING, db_column='inst_code_fk', blank=True, null=True)
    metadata_fk = models.ForeignKey(Metadata, models.DO_NOTHING, db_column='metadata_fk', blank=True, null=True)
    perf_phys_name_fk = models.ForeignKey(PersonName, models.DO_NOTHING, db_column='perf_phys_name_fk', blank=True, null=True)
    study_fk = models.ForeignKey('Study', models.DO_NOTHING, db_column='study_fk')

    class Meta:
        managed = False
        db_table = 'series'
        unique_together = (('study_fk', 'series_iuid'),)


class SeriesQueryAttrs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    availability = models.IntegerField(blank=True, null=True)
    num_instances = models.IntegerField(blank=True, null=True)
    retrieve_aets = models.CharField(max_length=255, blank=True, null=True)
    cuids_in_series = models.CharField(max_length=255, blank=True, null=True)
    view_id = models.CharField(max_length=255, blank=True, null=True)
    series_fk = models.ForeignKey(Series, models.DO_NOTHING, db_column='series_fk')

    class Meta:
        managed = False
        db_table = 'series_query_attrs'
        unique_together = (('view_id', 'series_fk'),)


class SeriesReq(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accession_no = models.CharField(max_length=255)
    req_proc_id = models.CharField(max_length=255)
    req_service = models.CharField(max_length=255)
    sps_id = models.CharField(max_length=255)
    study_iuid = models.CharField(max_length=255)
    accno_issuer_fk = models.ForeignKey(Issuer, models.DO_NOTHING, db_column='accno_issuer_fk', blank=True, null=True)
    req_phys_name_fk = models.ForeignKey(PersonName, models.DO_NOTHING, db_column='req_phys_name_fk', blank=True, null=True)
    series_fk = models.ForeignKey(Series, models.DO_NOTHING, db_column='series_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series_req'


class SoundexCode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sx_code_value = models.CharField(max_length=255)
    sx_pn_comp_part = models.IntegerField()
    sx_pn_comp = models.IntegerField()
    person_name_fk = models.ForeignKey(PersonName, models.DO_NOTHING, db_column='person_name_fk')

    class Meta:
        managed = False
        db_table = 'soundex_code'


class SpsStationAet(models.Model):
    mwl_item_fk = models.ForeignKey(MwlItem, models.DO_NOTHING, db_column='mwl_item_fk')
    station_aet = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sps_station_aet'


class StgcmtResult(models.Model):
    id = models.BigIntegerField(primary_key=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    device_name = models.CharField(max_length=255)
    exporter_id = models.CharField(max_length=255, blank=True, null=True)
    msg_id = models.CharField(max_length=255, blank=True, null=True)
    num_failures = models.IntegerField(blank=True, null=True)
    num_instances = models.IntegerField(blank=True, null=True)
    series_iuid = models.CharField(max_length=255, blank=True, null=True)
    sop_iuid = models.CharField(max_length=255, blank=True, null=True)
    stgcmt_status = models.IntegerField()
    study_iuid = models.CharField(max_length=255)
    transaction_uid = models.CharField(unique=True, max_length=255)
    updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stgcmt_result'


class StgverTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    completed = models.IntegerField()
    created_time = models.DateTimeField()
    failed = models.IntegerField()
    local_aet = models.CharField(max_length=255)
    series_iuid = models.CharField(max_length=255, blank=True, null=True)
    sop_iuid = models.CharField(max_length=255, blank=True, null=True)
    storage_ids = models.CharField(max_length=255, blank=True, null=True)
    stgcmt_policy = models.IntegerField(blank=True, null=True)
    study_iuid = models.CharField(max_length=255)
    update_location_status = models.BooleanField(blank=True, null=True)
    updated_time = models.DateTimeField()
    queue_msg_fk = models.ForeignKey(QueueMsg, models.DO_NOTHING, db_column='queue_msg_fk', verbose_name="QueueMsg")

    class Meta:
        managed = False
        db_table = 'stgver_task'


class Study(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access_control_id = models.CharField(max_length=255)
    access_time = models.DateTimeField()
    accession_no = models.CharField(max_length=255)
    completeness = models.IntegerField()
    created_time = models.DateTimeField()
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    expiration_exporter_id = models.CharField(max_length=255, blank=True, null=True)
    expiration_state = models.IntegerField()
    ext_retrieve_aet = models.CharField(max_length=255)
    failed_retrieves = models.IntegerField()
    modified_time = models.DateTimeField()
    rejection_state = models.IntegerField()
    study_size = models.BigIntegerField()
    storage_ids = models.CharField(max_length=255, blank=True, null=True)
    study_custom1 = models.CharField(max_length=255)
    study_custom2 = models.CharField(max_length=255)
    study_custom3 = models.CharField(max_length=255)
    study_date = models.CharField(max_length=255)
    study_desc = models.CharField(max_length=255)
    study_id = models.CharField(max_length=255)
    study_iuid = models.CharField(unique=True, max_length=255)
    study_time = models.CharField(max_length=255)
    updated_time = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    dicomattrs_fk = models.ForeignKey(Dicomattrs, models.DO_NOTHING, db_column='dicomattrs_fk', verbose_name="Dicomattrs")
    accno_issuer_fk = models.ForeignKey(Issuer, models.DO_NOTHING, db_column='accno_issuer_fk', blank=True, null=True)
    patient_fk = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_fk')
    ref_phys_name_fk = models.ForeignKey(PersonName, models.DO_NOTHING, db_column='ref_phys_name_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study'


class StudyQueryAttrs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    availability = models.IntegerField(blank=True, null=True)
    mods_in_study = models.CharField(max_length=255, blank=True, null=True)
    num_instances = models.IntegerField(blank=True, null=True)
    num_series = models.IntegerField(blank=True, null=True)
    retrieve_aets = models.CharField(max_length=255, blank=True, null=True)
    cuids_in_study = models.CharField(max_length=255, blank=True, null=True)
    view_id = models.CharField(max_length=255, blank=True, null=True)
    study_fk = models.ForeignKey(Study, models.DO_NOTHING, db_column='study_fk')

    class Meta:
        managed = False
        db_table = 'study_query_attrs'
        unique_together = (('view_id', 'study_fk'),)


class Uidmap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uidmap = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'uidmap'


class VerifyObserver(models.Model):
    id = models.BigIntegerField(primary_key=True)
    verify_datetime = models.CharField(max_length=255)
    observer_name_fk = models.ForeignKey(PersonName, models.DO_NOTHING, db_column='observer_name_fk', blank=True, null=True)
    instance_fk = models.ForeignKey(Instance, models.DO_NOTHING, db_column='instance_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verify_observer'
