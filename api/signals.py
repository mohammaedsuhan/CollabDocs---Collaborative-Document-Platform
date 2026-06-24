from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='api.Document')
def create_document_audit_log(sender, instance, created, **kwargs):
    """Write an AuditLog entry every time a Document is saved."""
    from api.models import AuditLog  # local import avoids circular dependency

    action = 'created' if instance._state.adding or created else 'updated'
    AuditLog.objects.create(
        actor=instance.created_by,
        action=action,
        model_name='Document',
        object_id=instance.pk,
    )