from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Project:

    project_id: str

    project_name: str

    description: str = ""

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    pdfs: list = field(default_factory=list)