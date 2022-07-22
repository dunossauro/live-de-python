-- Running downgrade b723047f6d98 -> 4c23117c5483

ALTER TABLE pessoa2 DROP COLUMN idade;

UPDATE alembic_version SET version_num='4c23117c5483' WHERE alembic_version.version_num = 'b723047f6d98';

-- Running downgrade 4c23117c5483 -> 8655b1ac0ebb

DROP TABLE pessoa2;

UPDATE alembic_version SET version_num='8655b1ac0ebb' WHERE alembic_version.version_num = '4c23117c5483';

-- Running downgrade 8655b1ac0ebb -> eb9562d19265

ALTER TABLE pessoa DROP COLUMN senha;

UPDATE alembic_version SET version_num='eb9562d19265' WHERE alembic_version.version_num = '8655b1ac0ebb';

