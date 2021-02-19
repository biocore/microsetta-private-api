from microsetta_private_api.LEGACY.sql_connection import TRN
from microsetta_private_api.db.migration_support import MigrationSupport

with TRN:
    MigrationSupport.migrate_76(TRN)
    TRN.rollback()