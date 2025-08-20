import gettext

t = gettext.translation('messages', localedir='locale', fallback=True)

t.install()

number_of_messages = 1

if not number_of_messages:
    print(t.gettext('No new messages'))
else:
    print(
        t.ngettext(
            'You have %(count)d message',
            'You have %(count)d message',
            number_of_messages
        ) % {'count': number_of_messages}
    )
