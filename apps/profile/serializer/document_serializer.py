from rest_framework import serializers

from apps.common.serializers.document_type import DocumentTypeSerializer
from apps.profile.models.document import Document


class DocumentSerializer(serializers.ModelSerializer):
    type = DocumentTypeSerializer()

    class Meta:
        model = Document
        fields = ['user', 'type']
