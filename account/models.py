from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# from hashlib import md5


class CustomerUser(models.Model):
    user = models.OneToOneField(User,
                                related_name='customeruser',
                                on_delete=models.CASCADE)
    secondary_email = models.EmailField(blank=True, unique=True, null=True)
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )


    """
    def save(self, *args, **kwargs):
        # ... other things not important here
        self.email = self.email.lower().strip()  # Hopefully reduces junk to ""
        if self.email != "":  # If it's not blank
            if not email_re.match(self.email)  # If it's not an email address
                raise ValidationError(u'%s is not an email address, dummy!' % self.email)
        if self.email == "":
            self.email = None
        super(Contact, self).save(*args, **kwargs)
    """


class VendorUser(models.Model):
    user = models.OneToOneField(User,
                                related_name='vendoruser',
                                on_delete=models.CASCADE)

    secondary_email = models.EmailField(_('secondary email address'), blank=True, null=True)
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.user.username


class Market(models.Model):
    belong_to = models.ForeignKey(
        to=VendorUser,
        related_name='Market',
        on_delete=models.CASCADE
    )

    market_name = models.CharField(max_length=30, unique=True, null=True, blank=True)
    created_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/%H/%M/%S')

    def __str__(self):
        return self.market_name


"""
def gravatar(self, size=80):
    md5_digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(md5_digest, size)

User.add_to_class(
    'gravatar',
    gravatar
)
"""
