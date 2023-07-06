
 
# United Nations Directories
# for Electronic Data Interchange for
# Administration, Commerce and Transport

# UN/EDIFACT


# Change indicators

# a plus sign (+)    for an addition
# an asterisk (*)    for an amendment to structure
# a hash sign (#)    for changes to names
# a vertical bar (|) for changes to text for descriptions and
#                     notes
# a minus sign (-)   for marked for deletion (within either
#                     batch and interactive messages)
# a X sign (X)       for marked for deletion (within both batch
#                     and interactive messages)

# 1225  Message function code                                   [C]

# Desc: Code indicating the function of the message.

# Data Element Cross Reference

# DataElement 1225 is used in the following Batch Segments:   BGM
# DataElement 1225 is used in the following Interactive Segments: CLT
# DataElement 1225 is used in the following Interactive Composite Elements:   E031    E972

# 1 .. 69

__description_name_code = (
"""
Cancellation
Message cancelling a previous transmission for a given
transaction.
"""
,
"""
Addition
Message containing items to be added.
"""
,
"""
Deletion
Message containing items to be deleted.
"""
,
"""
Change
Message containing items to be changed.
"""
,
"""
Replace
Message replacing a previous message.
"""
,
"""
Confirmation
Message confirming the details of a previous
transmission where such confirmation is required or
recommended under the terms of a trading partner
agreement.
"""
,
"""
Duplicate
The message is a duplicate of a previously generated
message.
"""
,
"""
Status
Code indicating that the referenced message is a status.
"""
,
"""
Original
Initial transmission related to a given transaction.
"""
,
"""
Not found
Message whose reference number is not filed.
"""
,
"""
Response
Message responding to a previous message or document.
"""
,
"""
Not processed
Message indicating that the referenced message was
received but not yet processed.
"""
,
"""
Request
Code indicating that the referenced message is a
request.
"""
,
"""
Advance notification
Code indicating that the information contained in the
message is an advance notification of information to
follow.
"""
,
"""
Reminder
Repeated message transmission for reminding purposes.
"""
,
"""
Proposal
Message content is a proposal.
"""
,
"""
Cancel, to be reissued
Referenced transaction cancelled, reissued message will
follow.
"""
,
"""
Reissue
New issue of a previous message (maybe cancelled).
"""
,
"""
Seller initiated change
Change information submitted by buyer but initiated by
seller.
"""
,
"""
Replace heading section only
Message to replace the heading of a previous message.
"""
,
"""
Replace item detail and summary only
Message to replace item detail and summary of a previous
message.
"""
,
"""
Final transmission
Final message in a related series of messages together
making up a commercial, administrative or transport
transaction.
"""
,
"""
Transaction on hold
Message not to be processed until further release
information.
"""
,
"""
Delivery instruction
Delivery schedule message only used to transmit short-
term delivery instructions.
"""
,
"""
Forecast
Delivery schedule message only used to transmit long-
term schedule information.
"""
,
"""
Delivery instruction and forecast
Combination of codes '24' and '25'.
"""
,
"""
Not accepted
Message to inform that the referenced message is not
accepted by the recipient.
"""
,
"""
Accepted, with amendment in heading section
Message accepted but amended in heading section.
"""
,
"""
Accepted without amendment
Referenced message is entirely accepted.
"""
,
"""
Accepted, with amendment in detail section
Referenced message is accepted but amended in detail
section.
"""
,
"""
Copy
Indicates that the message is a copy of an original
message that has been sent, e.g. for action or
information.
"""
,
"""
Approval
A message releasing an existing referenced message for
action to the receiver.
"""
,
"""
Change in heading section
Message changing the referenced message heading section.
"""
,
"""
Accepted with amendment
The referenced message is accepted but amended.
"""
,
"""
Retransmission
Change-free transmission of a message previously sent.
"""
,
"""
Change in detail section
Message changing referenced detail section.
"""
,
"""
Reversal of a debit
Reversal of a previously posted debit.
"""
,
"""
Reversal of a credit
Reversal of a previously posted credit.
"""
,
"""
Reversal for cancellation
Code indicating that the referenced message is reversing
a cancellation of a previous transmission for a given
transaction.
"""
,
"""
Request for deletion
The message is given to inform the recipient to delete
the referenced transaction.
"""
,
"""
Finishing/closing order
Last of series of call-offs.
"""
,
"""
Confirmation via specific means
Message confirming a transaction previously agreed via
other means (e.g. phone).
"""
,
"""
Additional transmission
Message already transmitted via another communication
channel. This transmission is to provide electronically
processable data only.
"""
,
"""
Accepted without reserves
Message accepted without reserves.
"""
,
"""
Accepted with reserves
Message accepted with reserves.
"""
,
"""
Provisional
Message content is provisional.
"""
,
"""
Definitive
Message content is definitive.
"""
,
"""
Accepted, contents rejected
Message to inform that the previous message is received,
but it cannot be processed due to regulations, laws,
etc.
"""
,
"""
Settled dispute
The reported dispute is settled.
"""
,
"""
Withdraw
Message withdrawing a previously approved message.
"""
,
"""
Authorisation
Message authorising a message or transaction(s).
"""
,
"""
Proposed amendment
A code used to indicate an amendment suggested by the
sender.
"""
,
"""
Test
Code indicating the message is to be considered as a
test.
"""
,
"""
Extract
A subset of the original.
"""
,
"""
Notification only
The receiver may use the notification information for
analysis only.
"""
,
"""
Advice of ledger booked items
An advice that items have been booked in the ledger.
"""
,
"""
Advice of items pending to be booked in the ledger
An advice that items are pending to be booked in the
ledger.
"""
,
"""
Pre-advice of items requiring further information
A pre-advice that items require further information.
"""
,
"""
Pre-adviced items
A pre-advice of items.
"""
,
"""
No action since last message
Code indicating the fact that no action has taken place
since the last message.
"""
,
"""
Complete schedule
The message function is a complete schedule.
"""
,
"""
Update schedule
The message function is an update to a schedule.
"""
,
"""
Not accepted, provisional
Not accepted, subject to confirmation.
"""
,
"""
Verification
The message is transmitted to verify information.
"""
,
"""
Unsettled dispute
To report an unsettled dispute.
"""
,
"""
Discharge of operation guarantee
A message related to a guarantee containing information
about the discharge of an operation.
"""
,
"""
Termination of operation guarantee
A message related to a guarantee containing information
about the termination of an operation.
"""
,
"""
Start of operation guarantee
A message related to a guarantee containing information
about the start of an operation.
"""
,
"""
Advanced cargo information
A message related to a guarantee containing advanced
cargo information.
"""
)


def get_description(postition):
    postition = int(postition)
    postition -= 1
    # print('Message function:')
    try:
        return __description_name_code[postition]
    except:
        return ''

# print(get_description('9'))