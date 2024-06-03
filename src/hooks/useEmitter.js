import { onUnmounted, getCurrentInstance } from 'vue';

export function useEmitter() {
  const instance = getCurrentInstance();
  const emitter = instance.appContext.config.globalProperties.emitter;

  onUnmounted(() => {
    emitter.off();
  });

  return emitter;
}