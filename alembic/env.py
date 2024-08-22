from logging.config import fileConfig
from alembic import context
from app.db.session import engine
from app.db.base_class import Base

# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)

# Set the target metadata for Alembic migrations
target_metadata = Base.metadata

# Import the models so that Base.metadata is updated with them
# This ensures that the models are part of the metadata and will be included in migrations
def include_models():
    Base.metadata.create_all(bind=engine)

def run_migrations_offline():
    include_models()  # Ensure models are included in metadata
    context.configure(url=str(engine.url), target_metadata=target_metadata, literal_binds=True)
    
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    include_models()  # Ensure models are included in metadata
    connectable = engine

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
