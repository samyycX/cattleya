<template>
  <div id="mdx-content-container">
    <Content />
  </div>
</template>

<script setup>
import { evaluate } from '@mdx-js/mdx';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import rehypeStarryNight from 'rehype-starry-night'
import { defineAsyncComponent, defineProps, defineEmits, watch } from 'vue';
import * as runtime from 'vue/jsx-runtime';
import '@/assets/css/tritanopia-dark.css';

const props = defineProps(['content'])
const emit = defineEmits(['renderComplete'])
var Content = renderBlog(); 
function renderBlog() {
  return defineAsyncComponent({ 
    loader: async () => {
      return new Promise((resolve, reject) => {
          try {
            evaluate(props.content, { 
              ...runtime,
              remarkPlugins: [ remarkMath, remarkGfm ],
              rehypePlugins: [ rehypeKatex, rehypeStarryNight ]
            }).then((content) => {
              resolve(content.default);
              emit("renderComplete")
            }).catch(() => {
              reject();
            });
          } catch (error) {
            reject();
          }
      });
    },
    onError() {}
  })
}

watch(props, async () => {
  Content = renderBlog();
});

</script>

<style scoped>
  
</style>
