<template>
  <q-item
    multiline
    :class="{ isUnread: message.isUnread }"
    class="conversation-message"
    highlight
  >
    <q-item-side>
      <ProfilePicture
        :user="message.author"
        :size="40"
      />
    </q-item-side>
    <q-item-main>
      <q-item-tile class="row no-wrap justify-between items-center">
        <div class="no-wrap">
          <router-link :to="{ name: 'user', params: { userId: message.author.id } }">
            <span class="text-bold text-secondary uppercase">{{ message.author.displayName }}</span>
          </router-link>
          <span class="message-date">
            <small class="light-paragraph">
              <DateAsWords :date="message.createdAt" />
            </small>
          </span>
          <q-icon
            v-if="message.receivedVia === 'email'"
            name="far fa-envelope"
            class="email-icon"
          >
            <q-tooltip v-t="'WALL.RECEIVED_VIA_EMAIL'" />
          </q-icon>
        </div>
        <ConversationAddReaction
          class="add-button reaction-box self-start"
          :reacted="currentUserReactions"
          @toggle="toggleReaction"
        />
      </q-item-tile>
      <Markdown
        :source="message.content"
        class="content"
      />
      <ConversationReactions
        v-if="hasReactions"
        :reactions="message.reactions"
        :current-user-reactions="currentUserReactions"
        @toggle="toggleReaction"
        style="margin-top: -3px"
      />
    </q-item-main>
  </q-item>
</template>

<script>
import ProfilePicture from '@/components/ProfilePictures/ProfilePicture'
import ConversationReactions from '@/components/Conversation/ConversationReactions'
import { QItem, QItemSide, QItemMain, QItemTile, QIcon, QTooltip } from 'quasar'
import DateAsWords from '@/components/General/DateAsWords'
import Markdown from '@/components/Markdown'
import ConversationAddReaction from './ConversationAddReaction'
export default {
  name: 'ConversationMessage',
  components: {
    ConversationReactions, ConversationAddReaction, ProfilePicture, QItem, QItemSide, QItemMain, QItemTile, DateAsWords, QIcon, QTooltip, Markdown,
  },
  props: {
    message: {
      type: Object,
      required: true,
    },
  },
  methods: {
    toggleReaction (name) {
      this.$emit('toggleReaction', { name, messageId: this.message.id })
    },
  },
  computed: {
    currentUserReactions () {
      return this.message && this.message.reactions && this.message.reactions.filter(e => e.reacted).map(e => e.name)
    },
    hasReactions () {
      return this.message && this.message.reactions && this.message.reactions.length > 0
    },
  },
}
</script>

<style scoped lang="stylus">
@import '~variables'
@import './reactionBox'

// same as PickupItem colors
$lightGreen = #E7FFE0
$lighterGreen = #F0FFF0

.left
  margin-right 1em
.content
  word-wrap break-word
.message-date
  display inline-block
  margin-left 2px
.message-reactions
  float right
  color gray
  padding-bottom 0.1em
.isUnread
  background linear-gradient(to right, $lightGreen, $lighterGreen)
.conversation-message
  padding-bottom 0
  .add-button
    visibility hidden
  &:hover .add-button
    visibility visible
.q-item-highlight:hover
  background-color alpha($secondary, .1)
.email-icon
  position relative
  top -1.5px
  margin-left 2px
</style>

<style lang="stylus">
// needs to be unscoped because it matches inside rendered markdown
.conversation-message .parsed
  overflow-wrap break-word
  p
    margin-bottom 0.5rem
  h1
    font-size 1.6em
  h2
    font-size 1.3em
  h3
    font-size 1.2em
  h4
    font-size 1.1em
  h5, h6
    font-size 1em
  pre
    font-size 0.8em
    padding 3px
    background-color #ededed
    margin-top 0.5rem
    margin-bottom 0.5rem
    overflow-x auto
    overflow-wrap normal
    display block
  p > code
    font-size 0.8em
    padding-left 3px
    padding-right 3px
    background-color #ededed
    overflow-x auto
    overflow-wrap normal
    display block
  img:not(.emoji)
    max-height 150px
    max-width 300px
</style>
